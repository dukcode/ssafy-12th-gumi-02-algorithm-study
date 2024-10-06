dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def get_start_pos():
    for y in range(n):
        for x in range(n):
            if data[y][x] == 'X':
                return y, x
    return -1, -1


for tc in range(int(input())):
    n = int(input())
    data = [list(input()) for _ in range(n)]

    print(f'#{tc + 1}', end=" ")

    for _ in range(int(input())):
        c, commands = input().split()
        commands = list(commands)

        cy, cx = get_start_pos()
        direction = 0

        for command in commands:
            if command == "R":
                direction = (direction + 1) % 4
                continue
            if command == "L":
                direction = (direction + 4 - 1) % 4
                continue

            ny, nx = cy + dy[direction], cx + dx[direction]
            if command == "A" and 0 <= ny < n and 0 <= nx < n and data[ny][nx] != "T":
                cy, cx = ny, nx

        if data[cy][cx] == "Y":
            print("1", end=" ")
            continue
        print("0", end=" ")
    print()
