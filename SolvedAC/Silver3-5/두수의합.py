N = int(input())
array = list(map(int, input().split()))
M = int(input())

array.sort()
left, right = 0, N-1
result = 0
while left < right:
    total = array[left] + array[right]
    if total < M:
        left += 1
    elif total > M:
        right -= 1
    else:
        result += 1
        right -= 1
print(result)