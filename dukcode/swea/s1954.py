dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    board = [[0] * n for _ in range(n)]

    x = 0
    y = 0
    dir = 0
    for num in range(1, n * n + 1):
        board[y][x] = num

        ny = y + dirs[dir][0]
        nx = x + dirs[dir][1]

        if (ny < 0 or ny >= n or nx < 0 or nx >= n) or board[ny][nx] != 0:
            dir = (dir + 1) % 4

        y += dirs[dir][0]
        x += dirs[dir][1]

    print(f"#{tc}")
    for i in range(n):
        print(*board[i])
