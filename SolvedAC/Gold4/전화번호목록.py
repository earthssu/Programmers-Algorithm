M = int(input())
for _ in range(M):
    N = int(input())
    phone = []
    for _ in range(N):
        phone.append(input())

    phone.sort()
    flag = True
    for i in range(N-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            flag = False
            break

    if not flag:
        print("NO")
    else:
        print("YES")