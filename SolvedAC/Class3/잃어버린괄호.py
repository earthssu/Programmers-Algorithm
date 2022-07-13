import sys
# 덧셈 연산을 먼저 한 후 마지막에 뺄셈
oper = sys.stdin.readline().strip()
operation = list()
numbers = list()
num = ""
for p in oper:
    if p == '+' or p == '-':
        numbers.append(num)
        num = ""
        operation.append(p)
    else:
        num += p
numbers.append(num)

while '+' in operation:
    idx = operation.index('+')
    operation.pop(idx)
    num1 = int(numbers.pop(idx))
    num2 = int(numbers.pop(idx))
    numbers.insert(idx, num1 + num2)

while '-' in operation:
    idx = operation.index('-')
    operation.pop(idx)
    num1 = int(numbers.pop(idx))
    num2 = int(numbers.pop(idx))
    numbers.insert(idx, num1 - num2)

print(numbers[0])

# a = input().split('-')
# num = []
# for i in a:
#     cnt = 0
#     s = i.split('+')
#     for j in s:
#         cnt += int(j)
#     num.append(cnt)
# n = num[0]
# for i in range(1, len(num)):
#     n -= num[i]
# print(n)