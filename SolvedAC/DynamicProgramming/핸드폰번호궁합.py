A = list(input())
B = list(input())

arr = []
for a, b in zip(A, B):
    arr.append(int(a))
    arr.append(int(b))

while len(arr) > 2:
    for i in range(0, len(arr)-1):
        num = arr[i] + arr[i+1]
        if num >= 10:
            num = num - 10
        arr[i] = num
    del arr[-1]

print(str(arr[0])+str(arr[1]))