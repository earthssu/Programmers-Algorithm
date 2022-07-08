import sys

A, B = sys.stdin.readline().strip().split()
min_a = int(A.replace('6', '5'))
max_a = int(A.replace('5', '6'))
min_b = int(B.replace('6', '5'))
max_b = int(B.replace('5', '6'))

print(min_a+min_b, max_a+max_b)
