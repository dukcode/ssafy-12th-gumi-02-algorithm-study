import sys

sys.stdin = open("input.txt", "r")
dy = {"R": 0, "L": 0, "D": 1, "U": -1}  # 동 서 남 북
dx = {"R": 1, "L": -1, "D": 0, "U": 0}  # 동 서 남 북
tank = {"R": ">", "L": "<", "D": "v", "U": "^"}  # 동 서 남 북


def is_tank(tank):
    return tank == ">" or tank == "<" or tank == "v" or tank == "^"


def get_tank_dir(tank):
    if tank == ">":
        return "R"
    if tank == "<":
        return "L"
    if tank == "v":
        return "D"
    if tank == "^":
        return "U"


def in_range(y, x):
    return y >= 0 and y < h and x >= 0 and x < w


t = int(input())
for tc in range(1, t + 1):
    h, w = tuple(map(int, input().split()))

    board = []
    tank_y = -1
    tank_x = -1
    tank_dir = None
    for y in range(h):
        board.append([*input()])
        for x in range(w):
            if is_tank(board[y][x]):
                tank_dir = get_tank_dir(board[y][x])
                tank_y = y
                tank_x = x
                board[y][x] = "."

    n = int(input())
    commands = input()

    for command in commands:
        if command != "S":
            dir = command
            tank_dir = dir
            ny = tank_y + dy[dir]
            nx = tank_x + dx[dir]

            if not in_range(ny, nx):
                continue

            if board[ny][nx] != ".":
                continue

            tank_y = ny
            tank_x = nx
            continue

        bomb_y = tank_y
        bomb_x = tank_x
        while True:
            bomb_y += dy[tank_dir]
            bomb_x += dx[tank_dir]

            if not in_range(bomb_y, bomb_x):
                break

            if board[bomb_y][bomb_x] == "#":
                break

            if board[bomb_y][bomb_x] == "*":
                board[bomb_y][bomb_x] = "."
                break

    print(f"#{tc} ", end="")
    for y in range(h):
        for x in range(w):
            if y == tank_y and x == tank_x:
                print(tank[tank_dir], end="")
                continue
            print(board[y][x], end="")
        print()
