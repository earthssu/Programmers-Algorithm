max_idx = 0
max_num = 0
for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        max_idx = i + 1

print(max_num)
print(max_idx)