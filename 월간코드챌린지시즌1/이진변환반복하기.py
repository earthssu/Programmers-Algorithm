def binary(n):
    result = ""
    while n > 0:
        n, mod = divmod(n, 2)
        result += str(mod)

    return result[::-1]


def solution(s):
    count, zero = 0, 0

    while s != "1":
        tmp_s = s.replace("0", "")
        zero += len(s) - len(tmp_s)
        s = tmp_s
        s = binary(len(s))
        count += 1

    return [count, zero]