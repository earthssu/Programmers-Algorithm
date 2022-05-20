num = 1
for i in range(3):
    a = int(input())
    num = num * a

num = str(num)
for n in range(10):
    print(num.count(str(n)))