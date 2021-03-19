def BinarySearch(left, right, m_list, target):
    while left <= right:
        mid = (left+right)//2
        if m_list[mid] == target:
            print(mid+1)
            break
        elif m_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


def BinarySearchRecursive(array, target, left, right):
    middle_idx = (left+right)//2
    print(middle_idx)
    middle = array[middle_idx]
    if target == middle:
        print('answer {}'.format(middle_idx))
    elif middle > target:
        BinarySearchRecursive(array, target,left,middle_idx-1)
    elif middle < target:
        BinarySearchRecursive(array, target,middle_idx+1,right)
    else:
        return False
