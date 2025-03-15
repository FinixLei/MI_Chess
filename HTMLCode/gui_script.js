/***************************************************
 *          Code Part 1 - Constants
 **************************************************/

const FIGHT_TYPE = {
    HUMAN_HUMAN: 'human-human',
    HUMAN_RED_AI_BLACK: 'human-red-ai-black',
    HUMAN_BLACK_AI_RED: 'human-black-ai-red',
    UNDEFINED: 'undefined'
}
const PIECE_COLOR = {
    RED: 'Red',
    BLACK: 'Black'
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

const RED_INIT_POSITIONS = {
    R1: 0,
    R2: 1,
    R3: 2
}

const BLACK_INIT_POSITIONS = {
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
 * 2. RED_POSITIONS: the positions of red stones in GUI_BOARD
 * 3. BLACK_POSITIONS: the positions of black stones in GUI_BOARD
 ********************************************************************************/

let GUI_BOARD = JSON.parse(JSON.stringify(INIT_BOARD))
let RED_POSITIONS = JSON.parse(JSON.stringify(RED_INIT_POSITIONS))
let BLACK_POSITIONS = JSON.parse(JSON.stringify(BLACK_INIT_POSITIONS))

let CURR_FIGHT_TYPE = FIGHT_TYPE.UNDEFINED;

let RED_TURN = true  // 开局红棋先走
let GAME_OVER = false  // 游戏是否结束

/********************************************************************************
 *                      Code Part 3 - Utility Functions
 *******************************************************************************/

/**
 * 
 * @param {目标位置的x坐标} x 
 * @param {目标位置的y坐标} y 
 * @param {要移动的棋子} pieceId 
 * @returns 
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
    // 找到当前棋子的位置
    for (let i = 0; i < GUI_BOARD.length; i++) {
        if (GUI_BOARD[i] == pieceId) {
            GUI_BOARD[i] = EMPTY;
            break;
        }
    }

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
    
    RED_TURN = !RED_TURN;

    // 更新棋盘棋子数据结构三变量
    GUI_BOARD[i] = pieceId;
    if (RED_STONES.includes(pieceId)) {
        RED_POSITIONS[pieceId] = i;
    }
    else if (BLACK_STONES.includes(pieceId)) {
        BLACK_POSITIONS[pieceId] = i;
    }
    else {
        alert("没发现这个棋子: ", pieceId);
    }
}

function checkWin() {
    let redPositionList = Object.values(RED_POSITIONS);
    redPositionList.sort();
    let lineNum = 1  // 忽略红棋位于[0,1,2]的情况
    for (; lineNum < LINES.length; lineNum++) {
        let line = LINES[lineNum];
        let win = true;
        for(let i=0; i<3; i++) {
            if (line[i] != redPositionList[i]) {
                win = false;
                continue;
            }
        }
        if (win) {
            alert("红方获胜！");
            GAME_OVER = true;
            return;
        }
    }

    let blackPositionList = Object.values(BLACK_POSITIONS);
    blackPositionList.sort();
    for (lineNum = 0; lineNum < LINES.length; lineNum++) {
        if (lineNum == 2) continue;  // 忽略黑棋位于[6,7,8]的情况
        let line = LINES[lineNum];
        let win = true;
        for(let i=0; i<3; i++) {
            if (line[i] != blackPositionList[i]) {
                win = false;
                continue;
            }
        }
        if (win) {
            alert("黑方获胜！");
            GAME_OVER = true;
            return;
        }
    };
}

function resetPiecesPositions() {
    GAME_OVER = false;
    GUI_BOARD = JSON.parse(JSON.stringify(INIT_BOARD))
    RED_POSITIONS = JSON.parse(JSON.stringify(RED_INIT_POSITIONS))
    BLACK_POSITIONS = JSON.parse(JSON.stringify(BLACK_INIT_POSITIONS))
    RED_TURN = true;

    // 重置棋子的位置
    const pieces = document.querySelectorAll('.piece');
    pieces.forEach(piece => {
        const pieceId = piece.id;
        let positionIndex;
        if (RED_STONES.includes(pieceId)) {
            positionIndex = RED_POSITIONS[pieceId];
        } else if (BLACK_STONES.includes(pieceId)) {
            positionIndex = BLACK_POSITIONS[pieceId];
        }
        const newPosition = validPositions[positionIndex];
        piece.style.left = `${newPosition.x}px`;
        piece.style.top = `${newPosition.y}px`;
    });
}

/******************************************************************************
 *                     Code Part 4 - GUI
 *****************************************************************************/

document.addEventListener('DOMContentLoaded', () => {
    /**
     * Code Part 4-1:   添加棋子和棋盘的点击事件
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
        if (newPosition == null) {
            return;
        }
        else {
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
            }, 2);
        }
    });

    /***************************************************************
     *  Code Part 4-2: 按钮点击事件
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

        }
        else {
            CURR_FIGHT_TYPE = FIGHT_TYPE.UNDEFINED;
        }
        console.log("Current Fight Type is ", CURR_FIGHT_TYPE);
    });
});
