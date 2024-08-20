BLANK = 0
BLACK = 1
WHITE = 2

dy = (-1, -1, -1, 0, 0, 1, 1, 1)
dx = (-1, 0, 1, -1, 1, -1, 0, 1)


def draw(y, x, color):
    board[y][x] = color
    for dir in range(8):

        flip = True
        ny = y
        nx = x
        while True:
            ny += dy[dir]
            nx += dx[dir]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                flip = False
                break

            if board[ny][nx] == BLANK:
                flip = False
                break

            if board[ny][nx] == color:
                break

        while flip:
            ny -= dy[dir]
            nx -= dx[dir]

            if ny == y and nx == x:
                break

            board[ny][nx] = color


def count():
    cnt_white = 0
    cnt_black = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == BLACK:
                cnt_black += 1
                continue

            if board[y][x] == WHITE:
                cnt_white += 1

    return cnt_black, cnt_white


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    board = [[BLANK] * n for _ in range(n)]

    half = n // 2
    board[half][half] = board[half - 1][half - 1] = WHITE
    board[half - 1][half] = board[half][half - 1] = BLACK

    for _ in range(m):
        y, x, color = map(int, input().split())
        y -= 1
        x -= 1

        draw(y, x, color)

    print(f"#{tc}", *count())
