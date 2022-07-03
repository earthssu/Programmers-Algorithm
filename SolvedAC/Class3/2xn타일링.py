N = int(input())
arr = [0, 1, 2]

if N > 2:
    for i in range(3, N+1):
        arr.append((arr[i-1] + arr[i-2]) % 10007)

print(arr[N])
