// 定义 9 个有效落子位置的坐标
const validPositions = [
    // 第一排
    { x:  5, y: 5 },
    { x: 120, y: 5 },
    { x: 235, y: 5 },
    // 第二排
    { x:  5, y: 120 },
    { x: 120, y: 120 },
    { x: 235, y: 120 },
    // 第三排
    { x:  5, y: 235 },
    { x: 120, y: 235 },
    { x: 235, y: 235 }
];

const PIECE_DIAMETER = 35
const PIECE_RADIUS = 17.5
const BOARD_WIDTH = 270
const BOARD_HEIGHT = 270

function validatePosition(x, y) {
    for (const position of validPositions) {
        if (Math.abs(position.x - x) <= PIECE_DIAMETER && Math.abs(position.y - y) <= PIECE_DIAMETER) {
            return position;
        }
    }
    return null;
}

document.addEventListener('DOMContentLoaded', () => {
    const pieces = document.querySelectorAll('.piece');
    const board = document.querySelector('.board');
    let selectedPiece = null;
    let firstBoardClick = false

    // 为每个棋子添加点击事件监听器
    pieces.forEach(piece => {
        piece.addEventListener('click', () => {
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
        if (!selectedPiece) return;
        
        if (!firstBoardClick) {
            firstBoardClick = true;
        }
        else {  // firstBoardClick = true
            // 获取棋盘的边界矩形
            const rect = board.getBoundingClientRect();
            // 计算目标位置相对于棋盘左上角的坐标，并减去棋子宽度和高度的一半，使棋子中心对准点击位置
            let x = event.clientX - rect.left - selectedPiece.offsetWidth / 2;
            let y = event.clientY - rect.top - selectedPiece.offsetHeight / 2;

            new_position = validatePosition(x, y)
            if (new_position == null) {
                firstBoardClick = false;
                return;
            }
            else {
                x = new_position.x
                y = new_position.y
            }

            // alert("x=" + x + ", y=" + y)
            // 设置选中棋子的新位置
            selectedPiece.style.left = `${x}px`;
            selectedPiece.style.top = `${y}px`;
            // 恢复选中棋子的大小
            selectedPiece.style.transform = 'scale(1)';
            // 取消选中状态
            selectedPiece = null;
            firstBoardClick = false;
        }
    });
});