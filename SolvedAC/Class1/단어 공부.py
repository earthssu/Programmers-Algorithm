string = input().upper()
alpha_num = {}

for s in string:
    if s not in alpha_num.keys():
        alpha_num[s] = 1
    else:
        alpha_num[s] += 1

temp, cnt = [], 0
for a in alpha_num:
    if alpha_num[a] > cnt:
        cnt = alpha_num[a]
        temp = [a]
    elif alpha_num[a] == cnt:
        temp.append(a)

print(temp[0] if len(temp) == 1 else '?')
