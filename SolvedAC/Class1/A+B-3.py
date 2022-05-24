N = int(input())
arr = []

for i in range(N):
    num = list(map(int, input().split(" ")))
    arr.append(num)

for i in range(N):
    print(arr[i][0] + arr[i][1])