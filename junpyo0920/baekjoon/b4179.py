from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def is_edges(pos):
    y, x = pos
    if y == 0 or x == 0 or y == h - 1 or x == w - 1:
        return True
    return False


def fire_move(start):
    q = deque(start)
    visited = [[0] * w for _ in range(h)]
    for y, x in start:
        visited[y][x] = 1

    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < h and 0 <= nx < w and data[ny][nx] == '.' and not visited[ny][nx]:
                fire_data[ny][nx] = fire_data[cy][cx] + 1
                visited[ny][nx] = 1
                q.append((ny, nx))


def jihoon_move(start):
    q = deque([start])
    visited = [[0] * w for _ in range(h)]

    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < h and 0 <= nx < w and data[ny][nx] == '.' and not visited[ny][nx]:
                time = jihoon_data[cy][cx] + 1
                if time < fire_data[ny][nx]:

                    if is_edges((ny, nx)):
                        print(time + 1)
                        exit()
                    jihoon_data[ny][nx] = time
                    visited[ny][nx] = 1
                    q.append((ny, nx))


h, w = map(int, input().split())
data = [list(input()) for _ in range(h)]
fire_data = [[0xFFFFFFF] * w for _ in range(h)]
jihoon_data = [[0] * w for _ in range(h)]

j = ()
f = []
for y in range(h):
    for x in range(w):
        if data[y][x] == "J":
            if is_edges((y, x)):
                print(1)
                exit()
            j = (y, x)
        if data[y][x] == "F":
            fire_data[y][x] = 0
            f.append((y, x))

fire_move(f)
jihoon_move(j)

print("IMPOSSIBLE")
