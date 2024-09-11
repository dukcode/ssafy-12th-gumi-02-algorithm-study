MX = 987_654_321

# 상 우 하 좌
DELTA_Y = (-1, 0, 1, 0)
DELTA_X = (0, 1, 0, -1)

BLANK = 0
PROCESSOR = 1
WIRE = 2


def remove_wire(start, dir):
    y, x = start
    while in_range(y, x) and board[y][x] != PROCESSOR:
        board[y][x] = BLANK
        y += DELTA_Y[dir]
        x += DELTA_X[dir]


def in_range(y, x):
    return y >= 0 and y < n and x >= 0 and x < n


def connect_wire(start, dir):
    y, x = start

    can_connect = True
    wire_len = 0
    while True:
        ny = y + DELTA_Y[dir]
        nx = x + DELTA_X[dir]

        if not in_range(ny, nx):
            break

        if board[ny][nx] == WIRE or board[ny][nx] == PROCESSOR:
            can_connect = False
            break

        wire_len += 1
        board[ny][nx] = WIRE
        y, x = ny, nx

    end = (y, x)

    return can_connect, wire_len, end


def is_already_connected(processor):
    y, x = processor
    return y == 0 or y == n - 1 or x == 0 or x == n - 1


def solve(idx=0, wire_len=0, cnt=0):
    global max_cnt
    global min_len

    # base case
    if idx == len(processors):
        if cnt > max_cnt:
            max_cnt = cnt
            min_len = wire_len
        elif cnt == max_cnt:
            min_len = min(min_len, wire_len)
        return

    if idx - cnt > len(processors) - max_cnt:
        return

    if is_already_connected(processors[idx]):
        solve(idx + 1, wire_len, cnt + 1)
        return

    solve(idx + 1, wire_len, cnt)
    for dir in range(4):
        can_connect, wire_len_to_add, end_pos = connect_wire(processors[idx], dir)

        if can_connect:
            solve(idx + 1, wire_len + wire_len_to_add, cnt + 1)

        remove_wire(end_pos, (dir + 2) % 4)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    processors = []
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                continue
            processors.append((y, x))

    max_cnt = 0
    min_len = MX
    solve()
    print(f"#{tc} {min_len}")
