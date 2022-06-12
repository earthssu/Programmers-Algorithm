import sys


N = int(sys.stdin.readline())
arr = []
for i in range(N):
    age, name = sys.stdin.readline().strip().split(" ")
    arr.append((int(age), name))

sorted_arr = sorted(arr, key=lambda x: x[0])

for key, value in sorted_arr:
    print(key, value)