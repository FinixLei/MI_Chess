/***************************************************
 *          Code Part 1 - Constants
 **************************************************/

const FIGHT_TYPE = {
    HUMAN_HUMAN: 'human-human',
    HUMAN_RED_AI_BLACK: 'human-red-ai-black',
    HUMAN_BLACK_AI_RED: 'human-black-ai-red',
    UNDEFINED: 'undefined'
}

const ROUTING = {
    0: [1, 3, 4],
    1: [0, 2, 4],
    2: [1, 4, 5],
    3: [0, 4, 6],
    4: [0, 1, 2, 3, 5, 6, 7, 8],
    5: [2, 4, 8],
    6: [3, 4, 7],
    7: [4, 6, 8],
    8: [4, 5, 7]
}

const LINES = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

const R1 = 'R1';
const R2 = 'R2';
const R3 = 'R3';
const B1 = 'B1';
const B2 = 'B2';
const B3 = 'B3';
const EMPTY = 'E';

const RED_STONES   = [R1, R2, R3]
const BLACK_STONES = [B1, B2, B3]

const STONE_INIT_POSITIONS = {
    R1: 0,
    R2: 1,
    R3: 2,
    B1: 6,
    B2: 7,
    B3: 8
}

const INIT_BOARD = [R1, R2, R3, EMPTY, EMPTY, EMPTY, B1, B2, B3]

const MAX_SCORE = 1000
const MIN_SCORE = -1000


// 定义 9 个有效落子位置的坐标
const validPositions = [
    // 第一排
    { x:  5, y: 3 },
    { x: 120, y: 3 },
    { x: 234, y: 3 },
    // 第二排
    { x:  5, y: 118 },
    { x: 120, y: 118 },
    { x: 234, y: 118 },
    // 第三排
    { x:  5, y: 233 },
    { x: 120, y: 233 },
    { x: 234, y: 233 }
];

const PIECE_RADIUS = 17.5
const BOARD_WIDTH = 270
const BOARD_HEIGHT = 270

/********************************************************************************
 *                      Code Part 2 - Global Variables
 * Always maintain 3 variables
 * When GUI_BOARD changes, the other two must be changed accordingly
 * 1. GUI_BOARD: the board in GUI_BOARD
 * 2. STONE_POSITIONS: the positions of all the stones in GUI_BOARD
 * 3. RED_TURN: whether it is red's turn
 * 4. CURRR_FIGHT_TYPE: the type of the current fight
 * 5. GAME_OVER: whether the game is over
 ********************************************************************************/

let GUI_BOARD = JSON.parse(JSON.stringify(INIT_BOARD))
let STONE_POSITIONS = JSON.parse(JSON.stringify(STONE_INIT_POSITIONS))
let RED_TURN = true  // 开局红棋先走

let CURR_FIGHT_TYPE = FIGHT_TYPE.UNDEFINED;
let GAME_OVER = false  // 游戏是否结束

/********************************************************************************
 *                      Code Part 3 - Class definitions
 *******************************************************************************/

// 定义 Move 类
class Move {
    constructor(pieceId, from, to) {
        this.pieceId = pieceId; // 表示移动的棋子
        this.from = from;   // 表示棋子的起始位置
        this.to = to;       // 表示棋子的目标位置
    }

    isEqual(other) {
        return this.pieceId == other.pieceId && this.from == other.from && this.to == other.to;
    }

    toString() {
        return "Move: " + this.pieceId + " from " + this.from + " to " + this.to;
    }
}

// 定义 BoardCase 类
// BoardCase由棋盘数组、棋子位置数组、当前走棋方三者组成
class BoardCase {
    constructor(board, stonePositions, redTurn) {
        this.board = JSON.parse(JSON.stringify(board));
        this.stonePositions = JSON.parse(JSON.stringify(stonePositions));
        this.redTurn = redTurn;
    }

    // 自定义比较方法
    isEqual(other) {
        if (this.board.length != other.board.length) {
            return false;
        }
        for (let i = 0; i < this.board.length; i++) {
            if (this.board[i] != other.board[i]) {
                return false;
            }
        }
        if (this.redTurn!= other.redTurn) {
            return false;
        }
        return true;
    }
}

// 定义 MoveAndBoardCase 类
// 执行该Move实例之后，会达到boardcase所描绘的局面
class MoveAndBoardCase {
    constructor(move, boardCase) {
        console.assert(boardCase instanceof BoardCase);
        this.move = new Move(move.pieceId, move.from, move.to);
        this.boardcase = new BoardCase(boardCase.board, boardCase.stonePositions, boardCase.redTurn);
    }
}

/********************************************************************************
 *                      Code Part 4 - Utility Functions
 *******************************************************************************/

/**
 * 给定棋盘中的一个坐标，判断它是否是9个可以落子的位置之一
 * 
 * @param {int} x, 目标位置的x坐标
 * @param {int} y, 目标位置的y坐标
 * @param {str} pieceId, 要移动的棋子的id
 * @returns null 或者 validPosition数组中的一个元素，即一个有效位置
 */
function validatePosition(x, y, pieceId) {
    // 获取要移动的棋子的当前位置
    let currPositionIndex = null;
    for (let i = 0; i < GUI_BOARD.length; i++) {
        if (GUI_BOARD[i] == pieceId) {
            currPositionIndex = i;
            break;
        }
    }
    if (currPositionIndex == null) {
        alert("棋子", pieceId, "不在棋盘上")
        return null;
    }

    for (let i = 0; i < validPositions.length; i++) {
        if (Math.abs(validPositions[i].x - x) <= PIECE_RADIUS && Math.abs(validPositions[i].y - y) <= PIECE_RADIUS) {
            if (GUI_BOARD[i] == EMPTY) {  // 该位置为空
                // 继续检查两点是否处于线连接的两端
                if (ROUTING[currPositionIndex].includes(i)) {
                    return validPositions[i];
                }
                return null;                
            }
            else {  // 该位置已有棋子
                return null;
            }
        }
    }
    return null;
}

// Make a move on the board （走一步棋）
function makeMove(pieceId, newPosition) {
    // 清空棋盘上给定的棋子
    for (let i = 0; i < GUI_BOARD.length; i++) {
        if (GUI_BOARD[i] == pieceId) {
            GUI_BOARD[i] = EMPTY;  // 清空该位置
            break;
        }
    }

    // 查询新的棋子位置是否合理，若合理，则记录下它所对应的 validPositions 数组中的下标
    let i = 0;
    for (; i < validPositions.length; i++) {
        if (validPositions[i].x == newPosition.x && validPositions[i].y == newPosition.y) {
            break;
        }
    }
    if (i == validPositions.length) {
        console.log("Cannot find the piece: ", pieceId);
        return;
    }

    // 更新棋盘棋子行棋者三变量
    GUI_BOARD[i] = pieceId;
    if (RED_STONES.includes(pieceId) || BLACK_STONES.includes(pieceId)) {
        STONE_POSITIONS[pieceId] = i;
    }
    else {
        alert("没发现这个棋子: ", pieceId);
    }
    RED_TURN = !RED_TURN;
}

function checkRedWin(stonePostions) {
    let redPositionList = [stonePostions[R1], stonePostions[R2], stonePostions[R3]];
    redPositionList.sort();
    let lineId = 1  // 忽略红棋位于[0,1,2]的情况
    for (; lineId < LINES.length; lineId++) {
        let line = LINES[lineId];
        let win = true;
        for(let i=0; i<3; i++) {
            if (line[i] != redPositionList[i]) {
                win = false;
                continue;
            }
        }
        if (win) return true;
    }
    return false;
}

function checkBlackWin(stonePostions) {
    let blackPositionList = [stonePostions[B1], stonePostions[B2], stonePostions[B3]];
    blackPositionList.sort();
    for (let lineId = 0; lineId < LINES.length; lineId++) {
        if (lineId == 2) continue;  // 忽略黑棋位于[6,7,8]的情况
        let line = LINES[lineId];
        let win = true;
        for(let i=0; i<3; i++) {
            if (line[i] != blackPositionList[i]) {
                win = false;
                continue;
            }
        }
        if (win) return true;
    };
    return false;
}

function checkWin() { // 检查是否有一方获胜
    if (GAME_OVER) return;

    if (checkRedWin(STONE_POSITIONS)) {
        alert("红方获胜！");
        GAME_OVER = true;
        return;
    }
    if (checkBlackWin(STONE_POSITIONS)) {
        alert("黑方获胜！");
        GAME_OVER = true;
    }
}

function resetPiecesPositions() {
    GAME_OVER = false;
    GUI_BOARD = JSON.parse(JSON.stringify(INIT_BOARD))
    STONE_POSITIONS = JSON.parse(JSON.stringify(STONE_INIT_POSITIONS))
    RED_TURN = true;

    // 重置棋子的位置
    const pieces = document.querySelectorAll('.piece');
    pieces.forEach(piece => {
        const pieceId = piece.id;
        let positionIndex = -1;
        if (RED_STONES.includes(pieceId) || BLACK_STONES.includes(pieceId)) {
            positionIndex = STONE_POSITIONS[pieceId];
        }
        const newPosition = validPositions[positionIndex];
        piece.style.left = `${newPosition.x}px`;
        piece.style.top = `${newPosition.y}px`;
    });
}

/**
 * 检查一个移动是否合法
 * @param {BoardCase} boardcase, BoardCase 类的对象
 * @param {str} stone, 即 pieceId
 * @param {int} to, 棋盘上的目标位置
 * @returns {true or false}, means valid or invalid
 */
function validateMove(boardcase, stone, to) {
    // 目标位置若不为空，则移动非法
    if (boardcase.board[to] != EMPTY) {
        return false;
    }
    // 起始位置若不是该棋子，则移动非法
    let from = boardcase.stonePositions[stone];
    if (boardcase.board[from] != stone) {
        return false;
    }
    // 起始位置和目标位置之间是否有连线
    if (!ROUTING[from].includes(to)) {
        return false;
    }
    return true;
}

// 给出一个给定盘面下的所有走法以及对应的盘面
function genMovesAndBoardCases(boardcase) {
    console.assert(boardcase instanceof BoardCase);

    let movesAndBoardCases = [];
    let board = boardcase.board;
    let redTurn = boardcase.redTurn;
    let stonePositions = boardcase.stonePositions;

    Object.keys(stonePositions).forEach((stone) => {
        if (redTurn && !RED_STONES.includes(stone)) return;
        if (!redTurn && !BLACK_STONES.includes(stone)) return;

        let from = stonePositions[stone];
        let availablePositions = ROUTING[from];
        availablePositions.forEach((to) => {
            if (board[to] == EMPTY) {
                const new_move = new Move(stone, from, to);
                let new_board = JSON.parse(JSON.stringify(board));
                new_board[from] = EMPTY;
                new_board[to] = stone;
                let new_stonePositions = JSON.parse(JSON.stringify(stonePositions));
                new_stonePositions[stone] = to;
                const new_boardcase = new BoardCase(new_board, new_stonePositions, !redTurn);
                const newMoveAndBoardCase = new MoveAndBoardCase(new_move, new_boardcase);
                movesAndBoardCases.push(newMoveAndBoardCase);
            }
        });
    });
    return movesAndBoardCases;
}

/**
 * Min-Max算法
 * @return: score:int, the score of the board case
 * @return: move_list: A list of move sequence, including current move for current board case
 */
function minMax(boardcase, depth) {
    console.assert(boardcase instanceof BoardCase);
    if (checkRedWin(boardcase.stonePositions))return [MAX_SCORE, []];
    if (checkBlackWin(boardcase.stonePositions)) return [MIN_SCORE, []];
    if (depth === 0) return [0, []];

    let best_score = 0;
    let best_move = null;
    let best_move_list = [];

    if (boardcase.redTurn) {
        best_score = MIN_SCORE;
        let red_moves_and_board_cases = genMovesAndBoardCases(boardcase);
        if (red_moves_and_board_cases.length === 0) {
            best_score = 0;
        }
        for (let move_and_board_case of red_moves_and_board_cases) {
            console.assert(move_and_board_case instanceof MoveAndBoardCase);
            let curr_move = move_and_board_case.move;
            let curr_board_case = move_and_board_case.boardcase;
            let [curr_score, move_list] = minMax(curr_board_case, depth-1);
            if (curr_score > best_score || best_move === null) {
                best_score = curr_score;
                best_move = {...curr_move };
                best_move_list = [...move_list];
                if (curr_score === MAX_SCORE) {
                    break;
                }
            }
        }
    } else { // turn to black to play
        best_score = MAX_SCORE;
        let black_moves_and_board_cases = genMovesAndBoardCases(boardcase);
        if (black_moves_and_board_cases.length === 0) {
            best_score = 0;
        }
        for (let move_and_board_case of black_moves_and_board_cases) {
            console.assert(move_and_board_case instanceof MoveAndBoardCase);
            let curr_move = move_and_board_case.move;
            let curr_board_case = move_and_board_case.boardcase;
            let [curr_score, move_list] = minMax(curr_board_case, depth-1);
            if (curr_score < best_score || best_move === null) {
                best_score = curr_score;
                best_move = {...curr_move };
                best_move_list = [...move_list];
                if (curr_score === MIN_SCORE) {
                    break;
                }
            }
        }
    }
    best_move_list.push(best_move);
    return [best_score, best_move_list];
}

/**
 * Generate a move for the given board case
 * Note, this function calculate the depths from 5 to the given depth
 * If the search finds a winning move, it will return immediately
 * Why do this? 
 * Because when a killer move is found in depth 5 but if the search depth is 10, 
 * several other moves are also considered as killer moves but actually they are not, 
 * as they could waste several rounds and then execute the real killer move.
 * This way will make the generated move is not the real killer move, so that it cannot beat the opponent.
 * So we need to start from depth 5 and if a winning move is found, we return immediately.
 * 
 * @param {BoardCase} boardcase - the current board case
 * @param {number} depth - the depth of the search, default is 10
 * @returns {Array} - [stone: string, end_pos: number, score: number], or [null, -1, 0] if no available moves
 */
function genMove(boardcase, depth = 10) {
    console.assert(boardcase instanceof BoardCase);
    const redTurn = boardcase.redTurn;
    const least_depth = 5;
    if (depth < least_depth) depth = least_depth;

    let di = least_depth;
    let move = null;
    let score = 0;
    while (di <= depth) {
        console.log(`Engine is thinking for depth = ${di}...`);
        [score, move_list] = minMax(boardcase, di);
        if (move_list.length === 0) {
            return [null, -1, 0];
        }

        move = move_list[move_list.length - 1];
        if (score === MAX_SCORE && redTurn) {
            return [move.pieceId, move.to, score];
        } else if (score === MIN_SCORE && !redTurn) {
            return [move.pieceId, move.to, score];
        } else {
            di++;
        }
    }
    return [move.pieceId, move.to, score];
}

/******************************************************************************
 *                     Code Part 5 - GUI
 *****************************************************************************/

function engineDoMove() {
    console.log("Current Red Turn is ", RED_TURN);
    [stone, to, score] = genMove(new BoardCase(GUI_BOARD, STONE_POSITIONS, RED_TURN), 10);
    if (stone == null) {
        alert("No available moves! Pass!");
        RED_TURN = !RED_TURN;
        return;
    }
    // 执行数据结构上的移动操作
    makeMove(stone, validPositions[to]);

    // 更新 HTML 上棋子的位置
    const piece = document.getElementById(stone);
    if (piece) {
        const newPosition = validPositions[to];
        piece.style.left = `${newPosition.x}px`;
        piece.style.top = `${newPosition.y}px`;
    }

    // 使用 setTimeout 确保在浏览器渲染后再检查游戏是否结束
    setTimeout(() => {
        checkWin();
    }, 1);
}

document.addEventListener('DOMContentLoaded', () => {
    /**
     * Code Part 5.1:   添加棋子和棋盘的点击事件
     */

    // 为每个棋子添加点击事件监听器
    const pieces = document.querySelectorAll('.piece');
    const board = document.querySelector('.board');
    let selectedPiece = null;

    // 为每个棋子添加点击事件监听器
    pieces.forEach(piece => {
        piece.addEventListener('click', (event) => {
            // 阻止事件冒泡
            event.stopPropagation(); 

            // 若未选择对战模式，则返回
            if (CURR_FIGHT_TYPE == FIGHT_TYPE.UNDEFINED) return;
            if (GAME_OVER) return;

            // 若轮到红棋走，但点击的不是红棋，则返回
            if (RED_TURN && !RED_STONES.includes(piece.id)) return;
            // 若轮到黑棋走，但点击的不是黑棋，则返回
            if (!RED_TURN && !BLACK_STONES.includes(piece.id)) return;

            // 如果已有选中的棋子，先将其恢复原状，无论该棋子是否是自己
            if (selectedPiece) {
                selectedPiece.style.transform ='scale(1)';
            }

            if (selectedPiece == piece) { // 若点击的棋子是自己
                // 取消选中状态
                selectedPiece = null;
            } 
            else {
                // 选中当前点击的棋子
                selectedPiece = piece;
                // 放大选中的棋子
                selectedPiece.style.transform = 'scale(1.2)';
            }
        });
    });

    // 为棋盘添加点击事件监听器
    board.addEventListener('click', (event) => {
        if (GAME_OVER) return;
        if (!selectedPiece) return;
        
        // 获取点中的棋子ID
        const pieceId = selectedPiece.id;
        
        // 获取棋盘的边界矩形
        const rect = board.getBoundingClientRect();
        // 计算目标位置相对于棋盘左上角的坐标，并减去棋子宽度和高度的一半，使棋子中心对准点击位置
        let x = event.clientX - rect.left - selectedPiece.offsetWidth / 2;
        let y = event.clientY - rect.top - selectedPiece.offsetHeight / 2;

        var newPosition = validatePosition(x, y, pieceId)
        if (newPosition == null) return;

        makeMove(selectedPiece.id, newPosition);

        // 设置选中棋子的新位置
        selectedPiece.style.left = `${newPosition.x}px`;
        selectedPiece.style.top = `${newPosition.y}px`;
        // 恢复选中棋子的大小
        selectedPiece.style.transform = 'scale(1)';
        // 取消选中状态
        selectedPiece = null;

        // 使用 setTimeout 确保在浏览器渲染后再检查游戏是否结束
        setTimeout(() => {
            checkWin();
        }, 1);

        // 再次判断是否游戏结束
        if (GAME_OVER) return;

        console.log("Fight Type: " + CURR_FIGHT_TYPE + ", Red Turn: " + RED_TURN);

        // 如果是人机对战，且人执红，且轮到黑走，则生成一个Move并执行
        if (CURR_FIGHT_TYPE == FIGHT_TYPE.HUMAN_RED_AI_BLACK && !RED_TURN) {
            engineDoMove();
        }
        else if (CURR_FIGHT_TYPE == FIGHT_TYPE.HUMAN_BLACK_AI_RED && RED_TURN) {
            // 若是人机对战，且人执黑，且轮到红走，则生成一个Move并执行
            engineDoMove();
        }
    });

    /***************************************************************
     *  Code Part 5.2: 按钮点击事件
     * *************************************************************/

    // 获取按钮元素
    const human_human_btn = document.getElementById('human-human-button');
    const human_red_btn   = document.getElementById('human-red-ai-black-button');
    const human_black_btn = document.getElementById('ai-red-human-black-button');

    // 为 human-human-button 添加点击事件监听器
    human_human_btn.addEventListener('click', function() {
        // 修改 this 指向为当前按钮
        this.classList.toggle('disabled');

        if (this.classList.contains('disabled')) {
            CURR_FIGHT_TYPE = FIGHT_TYPE.HUMAN_HUMAN;
            resetPiecesPositions();
            // 检查”人机对战(人执红)"按钮是否为灰色，如果是则让其变亮
            if (human_red_btn.classList.contains('disabled')) {
                human_red_btn.classList.remove('disabled');
            }
            // 检查”人机对战(人执黑)"按钮是否为灰色，如果是则让其变亮
            if (human_black_btn.classList.contains('disabled')) {
                human_black_btn.classList.remove('disabled');
            }
        }
        else {
            CURR_FIGHT_TYPE = FIGHT_TYPE.UNDEFINED;
        }
        console.log("Current Fight Type is ", CURR_FIGHT_TYPE);
    });

    // 为 human-red-button 添加点击事件监听器
    human_red_btn.addEventListener('click', function () {
        // 切换按钮的 disabled 类
        this.classList.toggle('disabled');

        if (this.classList.contains('disabled')) {
            CURR_FIGHT_TYPE = FIGHT_TYPE.HUMAN_RED_AI_BLACK;
            resetPiecesPositions();
            // 检查人人对战按钮是否为灰色，如果是则让其变亮
            if (human_human_btn.classList.contains('disabled')) {
                human_human_btn.classList.remove('disabled');
            }
            // 检查"人机对战(人执黑)"按钮是否为灰色，如果是则让其变亮
            if (human_black_btn.classList.contains('disabled')) {
                human_black_btn.classList.remove('disabled');
            }
        }
        else {
            CURR_FIGHT_TYPE = FIGHT_TYPE.UNDEFINED;
        }
        console.log("Current Fight Type is ", CURR_FIGHT_TYPE);
    });

    // 为 human-black-button 添加点击事件监听器
    human_black_btn.addEventListener('click', function () {
        // 切换按钮的 disabled 类
        this.classList.toggle('disabled');

        if (this.classList.contains('disabled')) {
            CURR_FIGHT_TYPE = FIGHT_TYPE.HUMAN_BLACK_AI_RED;
            resetPiecesPositions();
            // 检查人人对战按钮是否为灰色，如果是则让其变亮
            if (human_human_btn.classList.contains('disabled')) {
                human_human_btn.classList.remove('disabled');
            }
            // 检查”人机对战(人执红)"按钮是否为灰色，如果是则让其变亮
            if (human_red_btn.classList.contains('disabled')) {
                human_red_btn.classList.remove('disabled');
            }
            engineDoMove();

        }
        else {
            CURR_FIGHT_TYPE = FIGHT_TYPE.UNDEFINED;
        }
        console.log("Current Fight Type is ", CURR_FIGHT_TYPE);
    });
});
