def quad(size, array, start, answer):
    if size == 1:
        answer[array[start[0]][start[1]]] += 1
        return

    able = True
    point = array[start[0]][start[1]]
    for i in range(start[0], start[0]+size):
        for j in range(start[1], start[1]+size):
            if point != array[i][j]:
                able = False
                break

    if not able:
        size = size//2
        quad(size, array, start, answer)
        quad(size, array, [start[0]+size, start[1]], answer)
        quad(size, array, [start[0], start[1]+size], answer)
        quad(size, array, [start[0]+size, start[1]+size], answer)
    else:
        answer[point] += 1
        return


def solution(arr):
    answer = [0, 0]
    quad(len(arr), arr, [0, 0], answer)

    return answer