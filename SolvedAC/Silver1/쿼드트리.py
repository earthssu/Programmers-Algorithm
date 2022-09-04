import sys

N = int(sys.stdin.readline())
trees = []
for _ in range(N):
    trees.append(list(map(int, list(sys.stdin.readline().strip()))))

result = ""


def qued(size, row, col):
    global result
    if size < 1:
        return

    total = 0
    for i in range(row, row+size):
        for j in range(col, col+size):
            total += trees[i][j]
    if total == pow(size, 2):
        result += "1"
    elif total == 0:
        result += "0"
    else:
        result += "("
        qued(size // 2, row, col)
        qued(size // 2, row, col+(size//2))
        qued(size // 2, row+(size//2), col)
        qued(size // 2, row+(size//2), col+(size//2))
        result += ")"


qued(N, 0, 0)

print(result)