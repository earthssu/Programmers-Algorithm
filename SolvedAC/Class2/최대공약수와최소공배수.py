a, b = map(int, input().split(" "))

# 최대 공약수
GCD = min(a, b)
while True:
    if a % GCD == 0 and b % GCD == 0:
        break
    GCD -= 1

# 최소 공배수
LCM = a * b // GCD

print(GCD)
print(LCM)