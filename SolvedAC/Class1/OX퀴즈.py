N = int(input())

for i in range(N):
    grade = list(input())
    cnt = 0
    result = 0
    for g in grade:
        if g == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)