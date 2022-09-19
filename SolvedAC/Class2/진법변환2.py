N, B = map(int, input().split())
exchange = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G',
    17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N',
    24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U',
    31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'
}


def base_change(number, n):
    result = ""
    if number == 0:
        return '0'
    while number > 0:
        number, mod = divmod(number, n)
        if mod >= 10:
            result += exchange[mod]
        else:
            result += str(mod)
    return result[::-1]


print(base_change(N, B))