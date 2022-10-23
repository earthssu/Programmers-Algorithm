import sys

N = int(sys.stdin.readline())
stair = []
dp = []
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

if N > 2:
    dp.append(stair[0])  # 첫 번째 계단을 밟음
    dp.append(max(stair[0]+stair[1], stair[1]))  # 연속 두 개 오르기, 건너뛰기
    dp.append(max(stair[0]+stair[2], stair[1]+stair[2]))  # 중간 하나 건너뛰기, 앞에 하나 건너뛰기
    for i in range(3, N):
        # 두 칸 이전 상태 (상관없는 애) + 현재 계단값 or 세 칸 이전 상태 (상관없는 애) + 현재 계단값+이전 계단값
        dp.append(max(dp[i-2]+stair[i], stair[i]+stair[i-1]+dp[i-3]))
    print(dp[N - 1])
else:
    if N == 1:
        print(stair[0])
    else:
        print(stair[0]+stair[1])