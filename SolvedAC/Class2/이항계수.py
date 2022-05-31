from itertools import combinations


N, K = map(int, input().split(" "))
arr = [i for i in range(N)]
print(len(list(combinations(arr, K))))
