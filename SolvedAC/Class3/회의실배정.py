import sys


N = int(sys.stdin.readline())
meeting = []
for _ in range(N):
    meet = tuple(map(int, sys.stdin.readline().split()))
    meeting.append(meet)

meeting.sort(key=lambda x: (x[1], x[0]))

result = 1 if meeting[0][1] != 0 else 0
end = meeting[0][1]
for i in range(1, len(meeting)):
    if meeting[i][0] >= end:
        end = meeting[i][1]
        result += 1

print(result)