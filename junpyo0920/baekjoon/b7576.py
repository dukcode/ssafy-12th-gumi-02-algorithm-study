from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def get_starts():
    ret = deque()
    for y in range(h):
        for x in range(w):
            if data[y][x] == 1:
                ret.append((y, x))
    return ret


def bfs(q):
    ret = 1
    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if (0 <= ny < h and 0 <= nx < w) and data[ny][nx] == 0:
                data[ny][nx] = data[cy][cx] + 1
                q.append((ny, nx))
                ret = data[ny][nx]
    for y in range(h):
        for x in range(w):
            if data[y][x] == 0:
                print(-1)
                return
    print(ret-1)


w, h = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]
bfs(get_starts())
