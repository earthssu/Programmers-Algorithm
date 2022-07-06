import sys


N, R, C = map(int, input().split())
count = 0


def divide(row, col, size):
    global count

    if row == R and col == C:
        print(count)
        sys.exit(0)

    if size == 1:
        count += 1
        return

    if not (row <= R < row + size and col <= C < col + size):
        count += (size * size)
        return

    s = size // 2
    divide(row, col, s)
    divide(row, col + s, s)
    divide(row + s, col, s)
    divide(row + s, col + s, s)


divide(0, 0, 2**N)