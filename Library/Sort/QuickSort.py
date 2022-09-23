def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [y for y in tail if y > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)