N = int(input())
# arr = {}
# for i in range(N):
#     s = input()
#     if len(s) in arr.keys():
#         arr[len(s)].append(s)
#     else:
#         arr[len(s)] = [s]
#
# sorted_arr = sorted(arr.items())
# new_dict = []
#
# for sa in sorted_arr:
#     sa[1].sort()
#     for s in sa[1]:
#         if s not in new_dict:
#             new_dict.append(s)
#
# for d in new_dict:
#     print(d)

arr = []
for i in range(N):
    arr.append(input())

arr = list(set(arr))
sort_arr = []
for i in arr:
    sort_arr.append((len(i), i))

result = sorted(sort_arr)
for key, value in result:
    print(value)