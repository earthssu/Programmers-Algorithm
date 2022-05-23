music = list(map(int, input().split(" ")))

diff = music[0] - music[1]
if diff != 1 and diff != -1:
    print("mixed")
else:
    for m in range(1, 7):
        if diff != music[m] - music[m+1]:
            print("mixed")
            break
    else:
        if diff == 1:
            print("descending")
        elif diff == -1:
            print("ascending")