def base_change(num, n):
    base = ''
    alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if num == 0:
        return '0'

    while num > 0:
        num, mod = divmod(num, n)
        if mod >= 10:
            base += alpha[mod]
        else:
            base += str(mod)

    return base[::-1]