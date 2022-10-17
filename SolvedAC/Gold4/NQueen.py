import sys

N = int(sys.stdin.readline())
queen = [0] * N
answer = 0


def is_promising(row):
    for i in range(row):
        if queen[row] == queen[i] or abs(queen[row] - queen[i]) == abs(row - i):
            return False
    return True

def n_queen(row):
    global answer
    if row == N:
        answer += 1
        return

    for i in range(N):
        queen[row] = i
        if is_promising(row):
            n_queen(row+1)


n_queen(0)

print(answer)