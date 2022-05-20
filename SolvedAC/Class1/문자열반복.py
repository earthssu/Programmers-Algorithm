N = int(input())
repeat_num = []
repeat_str = []

for i in range(N):
    n = input().split(" ")
    repeat_num.append(int(n[0]))
    repeat_str.append(n[1])

for i in range(N):
    for s in repeat_str[i]:
        print(s * repeat_num[i], end='')
    print()