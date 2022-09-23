def hanoi(n, from_pos, end_pos, mid_pos):
    if n == 1:
        print(from_pos, end_pos)
        return
    hanoi(n-1, from_pos, mid_pos, end_pos)
    print(from_pos, end_pos)
    hanoi(n-1, mid_pos, end_pos, from_pos)