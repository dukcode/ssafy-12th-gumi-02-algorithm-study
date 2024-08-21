from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs():
    q = deque([(0, 0)])
    data[0][0] = 1
    while q:
        cy, cx = q.popleft()
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < h and 0 <= nx < w and data[ny][nx] == 1:
                if ny == 0 and nx == 0: continue
                data[ny][nx] = data[cy][cx] + 1
                q.append((ny, nx))
    print(data[h-1][w-1])


h, w = map(int, input().split())
data = [list(map(int, input())) for _ in range(h)]
bfs()