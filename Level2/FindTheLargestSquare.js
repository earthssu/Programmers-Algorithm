function solution(board)
{
    const x_len = board[0].length;
    const y_len = board.length;
    let answer = 0;

    if(x_len < 2 || y_len < 2 ) return 1

    for (let i=1; i<y_len; i++) {
        for (let j=1; j<x_len; j++) {
            if (board[i][j] > 0) {
                const min = Math.min(board[i-1][j-1], board[i-1][j], board[i][j-1]);
                board[i][j] = min + 1
                if (answer < board[i][j]) answer = board[i][j];
            }
        }
    }

    return answer ** 2;
}