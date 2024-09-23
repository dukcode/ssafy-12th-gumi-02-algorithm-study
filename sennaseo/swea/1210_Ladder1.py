def solve(r, c):
    d = 0
    dr = [1, 0, 0]
    dc = [0, -1, 1]
    while r < 99:
        r += dr[d]
        c += dc[d]
        if d == 0:
            if c > 0 and ladder[r][c - 1] == 1:
                d = 1
            elif c < 99 and ladder[r][c + 1] == 1:
                d = 2
        else:
            if r < 99 and ladder[r + 1][c] == 1:
                d = 0
    if ladder[r][c] == 2:
        return True
    else:
        return False


for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder[0][i] == 1:
            if solve(0, i):
                print(f"#{tc} {i}")
                break
