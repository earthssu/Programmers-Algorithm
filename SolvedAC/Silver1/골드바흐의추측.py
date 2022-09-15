import sys

p_list = [True] * 1000000
m = 1000
for i in range(2, m+1):
    if p_list[i]:
        for j in range(i+i, 1000000, i):
            p_list[j] = False


while True:
    num = int(sys.stdin.readline())
    if num == 0:
        break
    flag = False
    for k in range(3, (num // 2) + 1):
        if p_list[k] and p_list[num-k]:
            flag = True
            print("{} = {} + {}".format(num, k, num-k))
            break

    if not flag:
        print("Goldbach's conjecture is wrong.")