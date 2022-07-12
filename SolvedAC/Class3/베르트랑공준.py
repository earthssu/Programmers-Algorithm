import sys

while True:
    start = int(sys.stdin.readline())
    if start == 0:
        break
    if start == 1:
        print(1)
    else:
        end = 2 * start
        # 에라토스테네스의 체 활용
        arr = [True] * end
        m = int(end ** 0.5)
        for i in range(2, m + 1):
            if arr[i]:
                for j in range(i * 2, end, i):
                    arr[j] = False
        arr = arr[start+1:]
        print(arr.count(True))