def solution(N, number):
    possible_set = [0, [N]]
    if N == number:
        return 1
    for i in range(2, 9):
        case_set = []
        basic_num = int(str(N) * i)
        case_set.append(basic_num)
        for i_half in range(1, i//2+1):
            for x in possible_set[i_half]:
                for y in possible_set[i - i_half]:
                    case_set.append(x+y)
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y != 0:
                        case_set.append(x/y)
                    if x != 0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            possible_set.append(case_set)
    return -1