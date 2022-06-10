def is_decimal(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False

    return True


N = int(input())
arr = list(map(int, input().split(" ")))
result = 0

for i in range(N):
    if is_decimal(arr[i]):
        result += 1

print(result)

