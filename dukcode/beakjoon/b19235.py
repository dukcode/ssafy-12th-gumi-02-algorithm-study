GREEN = 0
BLUE = 1
TYPE = ((0, 0), (0, 0), (0, 1), (1, 0))

H = 6
W = 4

EMPTY = 0
FULL = 1
NEITHER = 2


def add_block(t, pos, board, start_y):
    global num

    y = start_y
    while y + TYPE[t][0] != H and (
        board[y][pos] == 0 and board[y + TYPE[t][0]][pos + TYPE[t][1]] == 0
    ):
        y += 1
    y -= 1

    board[y][pos] = num
    board[y + TYPE[t][0]][pos + TYPE[t][1]] = num
    num += 1


def status(line):
    cnt_zero = 0
    for x in range(W):
        if line[x] == 0:
            cnt_zero += 1

    if cnt_zero == W:
        return EMPTY

    if cnt_zero == 0:
        return FULL

    return NEITHER


def get_full_lines(board):
    ret = []
    for y in range(H):
        if status(board[y]) == FULL:
            ret.append(y)

    return ret


def clear_lines(lines, board):
    for y in lines:
        board[y] = [0] * W


def drop(board):
    for y in range(H - 1, -1, -1):
        for x in range(W):
            if board[y][x] == 0:
                continue

            if y != H - 1 and board[y][x] == board[y + 1][x]:
                board[y][x] = board[y + 1][x] = 0
                add_block(3, x, board, y)
                continue

            if x != W - 1 and board[y][x] == board[y][x + 1]:
                board[y][x] = board[y][x + 1] = 0
                add_block(2, x, board, y)
                continue

            if board[y][x - 1] != board[y][x]:
                board[y][x] = 0
                add_block(1, x, board, y)


def clean_special_area(board):
    if status(board[0]) != EMPTY:
        for y in range(H - 1, 1, -1):
            board[y] = board[y - 2]
        board[0] = [0] * W
        board[1] = [0] * W
        return

    if status(board[1]) != EMPTY:
        for y in range(H - 1, 1, -1):
            board[y] = board[y - 1]
        board[1] = [0] * W
        return

    return


def put(t, pos, board):
    add_block(t, pos, board, 0)

    score = 0
    while lines := get_full_lines(board):
        score += len(lines)
        clear_lines(lines, board)
        drop(board)

    clean_special_area(board)

    return score


green = [[0] * W for _ in range(H)]
blue = [[0] * W for _ in range(H)]
num = 1

n = int(input())

score = 0
for _ in range(n):
    t, y, x = map(int, input().split())

    if t == 1:
        score += put(1, x, green)
        score += put(1, y, blue)
    elif t == 2:
        score += put(2, x, green)
        score += put(3, y, blue)
    else:  # t == 3
        score += put(3, x, green)
        score += put(2, y, blue)
print(score)

cnt = 0
for y in range(2, H):
    for x in range(W):
        if green[y][x] != 0:
            cnt += 1
        if blue[y][x] != 0:
            cnt += 1
print(cnt)
