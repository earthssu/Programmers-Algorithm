N, M = map(int, input().split())
sequence = list(map(int, input().split()))

left, right = 0, 1
result = 0
while left <= N and right <= N:
    add = sum(sequence[left:right])
    if add < M:
        right += 1
    elif add > M:
        left += 1
    else:
        result += 1
        right += 1

print(result)
