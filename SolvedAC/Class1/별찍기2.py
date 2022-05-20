N = int(input())

for i in range(1, N+1):
    star = ' ' * (N - i)
    star += '*' * i
    print(star)