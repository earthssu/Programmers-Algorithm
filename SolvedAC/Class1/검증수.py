num = map(int, input().split(" "))
pow_sum = 0

for n in num:
    pow_sum += n**2

print(pow_sum % 10)