import sys


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(' ')))

arr.sort()
sum_result = []
for i in range(1, len(arr)+1):
    sum_result.append(sum(arr[0:i]))

print(sum(sum_result))
