dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(board, visited, first_y, first_x):
    stk = [(first_y, first_x)]
    visited[first_y][first_x] = True

    while stk:
        cur_y, cur_x = stk.pop()
        for dir in dirs:
            ny = cur_y + dir[0]
            nx = cur_x + dir[1]

            if ny < 0 or ny >= w or nx < 0 or nx >= w:
                continue

            if visited[ny][nx] or board[ny][nx] == 0:
                continue

            visited[ny][nx] = True
            stk.append((ny, nx))


t = int(input())
for _ in range(t):
    w, h, k = tuple(map(int, input().split()))
    board = [[0] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    for i in range(k):
        x, y = tuple(map(int, input().split()))
        board[y][x] = 1

    cnt = 0

    for y in range(h):
        for x in range(w):
            if visited[y][x] or board[y][x] == 0:
                continue
            dfs(board, visited, y, x)
            cnt += 1

    print(cnt)
