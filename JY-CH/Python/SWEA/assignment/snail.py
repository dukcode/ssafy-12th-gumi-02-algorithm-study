t = int(input())
for tc in range(1, t+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]
    # 오른쪽, 아래, 왼쪽, 위로
    move_row = [0, 1, 0, -1]
    move_col = [1, 0, -1, 0]

    r, c = 0, 0
    m = 0
    num = 1
    while num <= n*n:
        arr[r][c] = num
        num += 1
        r += move_row[m]
        c += move_col[m]

        if r < 0 or r >= n or c < 0 or c >= n or arr[r][c]:
            r -= move_row[m]
            c -= move_col[m]
            m = (m + 1) % 4
            r += move_row[m]
            c += move_col[m]


    print(f'#{tc}')
    for row in arr:
        print(*row)