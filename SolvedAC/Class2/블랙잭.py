from itertools import combinations

N, M = map(int, input().split(" "))
num_arr = list(map(int, input().split(" ")))
comb = list(combinations(num_arr, 3))
result = 0

for c in comb:
    temp = sum(c)
    if M >= temp > result:
        result = temp

print(result)