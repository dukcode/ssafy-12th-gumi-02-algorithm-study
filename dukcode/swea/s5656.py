# 벽돌 깨기 (3초)
MX = 987_654_321

dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)


def count_bricks(board):
    ret = 0
    for y in range(h):
        for x in range(w):
            if board[y][x] != 0:
                ret += 1
    return ret


def copy(board):
    ret = [[0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            ret[y][x] = board[y][x]

    return ret


def get_first_y_idx(board, pos):
    for y in range(h):
        if board[y][pos] != 0:
            return y
    return -1


def shot(board, y, x, dist):

    board[y][x] = 0
    for dir in range(4):
        for d in range(1, dist):
            ny = y + dy[dir] * d
            nx = x + dx[dir] * d

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            shot(board, ny, nx, board[ny][nx])


def drop(board):
    for x in range(w):
        idx = h - 1
        for y in range(h - 1, -1, -1):
            if board[y][x] == 0:
                continue
            board[idx][x] = board[y][x]
            idx -= 1

        while idx >= 0:
            board[idx][x] = 0
            idx -= 1


def has_blick(board, pos):
    for y in range(h):
        if board[y][pos] != 0:
            return True
    return False


def solve(board, num_shot):
    if num_shot == 0:
        return count_bricks(board)

    ret = MX
    for x in range(w):
        y = get_first_y_idx(board, x)
        if y == -1:
            continue

        next_board = copy(board)
        shot(next_board, y, x, next_board[y][x])
        drop(next_board)
        ret = min(ret, solve(next_board, num_shot - 1))

    return ret


t = int(input())
for tc in range(1, t + 1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]

    ans = solve(board, n)
    if ans == MX:
        ans = 0

    print(f"#{tc} {ans}")
