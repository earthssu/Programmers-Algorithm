import sys
from itertools import permutations

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
oper_num = list(map(int, sys.stdin.readline().split()))
oper_list = ['+', '-', '*', '/']
calc = []
for num, list in zip(oper_num, oper_list):
    for i in range(num):
        calc.append(list)

results = []
total_calc = set(permutations(calc, N-1))
for tc in total_calc:
    tmp = numbers[0]
    for i in range(1, N):
        if tc[i-1] == '+':
            tmp += numbers[i]
        elif tc[i-1] == '-':
            tmp -= numbers[i]
        elif tc[i-1] == '*':
            tmp *= numbers[i]
        else:
            if tmp < 0:
                tmp = int(tmp / numbers[i])
            else:
                tmp = tmp // numbers[i]
    results.append(tmp)

print(max(results), min(results))


"""
dfs 풀이 
https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python
"""