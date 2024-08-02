UP = 0
RIGHT = 1
LEFT = 2

dirs = ((-1, 0), (0, 1), (0, -1))


def is_road(y, x):
    return (0 <= y < n and 0 <= x < n) and board[y][x]


n = 100
t = 10
for _ in range(t):
    tc = int(input())
    board = [list(map(int, input().strip().split())) for _ in range(n)]

    end_x = -1
    for idx, num in enumerate(board[n - 1]):
        if num == 2:
            end_x = idx
            break

    y = n - 1
    x = end_x
    dir = UP

    while True:
        if y == 0:
            break

        if dir == UP:
            if is_road(y, x - 1):
                dir = LEFT
            elif is_road(y, x + 1):
                dir = RIGHT
        else:
            if is_road(y - 1, x):
                dir = UP

        y += dirs[dir][0]
        x += dirs[dir][1]

    print(f"#{tc} {x}")
