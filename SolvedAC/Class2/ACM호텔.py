T = int(input())
answer = []

for i in range(T):
    H, W, N = map(int, input().split(" "))
    h = 0
    w = 1
    n = 0
    while n < N:
        n += 1  # 첫번째 손님부터 N번째 손님까지
        if h < H:
            h += 1
        else:
            h = 1
            w += 1

    ans = str(h)
    ans += str(w) if len(str(w)) > 1 else "0" + str(w)
    answer.append(ans)

for a in answer:
    print(a)