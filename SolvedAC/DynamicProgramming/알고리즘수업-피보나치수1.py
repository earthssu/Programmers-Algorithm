N = int(input())
cnt_fib, cnt_fibonacci = 0, 0

f = [0] * (N+1)
f[1], f[2] = 1, 1
for i in range(3, N+1):
    cnt_fibonacci += 1
    f[i] = f[i-1] + f[i-2]

cnt_fib = f[N]

print(cnt_fib, cnt_fibonacci)