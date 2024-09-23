from collections import deque
from heapq import heappop, heappush

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(start, marker):
    q = deque([start])
    visited[start[0]][start[1]] = 1
    data[start[0]][start[1]] = marker
    while q:
        cur_y, cur_x = q.popleft()
        for d in range(4):
            next_y, next_x = cur_y + dy[d], cur_x + dx[d]            
            if 0 <= next_y < h and 0 <= next_x < w and data[next_y][next_x] and not visited[next_y][next_x]:
                q.append((next_y, next_x))
                data[next_y][next_x] = marker
                visited[next_y][next_x] = 1


def get_edges(start):
    cur_y, cur_x = start
    for d in range(4):
        dis = 0
        next_y, next_x = cur_y + dy[d], cur_x + dx[d]

        while 0 <= next_y < h and 0 <= next_x < w and data[cur_y][cur_x] != data[next_y][next_x]:
            dis += 1

            if h <= next_y < 0 or w <= next_x < 0:
                break

            if data[next_y][next_x]:
                if dis > 2:
                    dis -= 1
                    heappush(adj_list, (dis, data[cur_y][cur_x], data[next_y][next_x]))
                break
            
            next_y += dy[d]
            next_x += dx[d]


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return find_set(p[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x < root_y:
        p[root_y] = root_x
    else:
        p[root_x] = root_y


h, w = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]

visited = [[0] * w for _ in range(h)]

marker = 0
for y in range(h):
    for x in range(w):
        if data[y][x] and not visited[y][x]:
            marker += 1
            bfs((y, x), marker)


adj_list = []

for y in range(h):
    for x in range(w):
        if data[y][x]:
            get_edges((y, x))

p = [x for x in range(marker + 1)]

ans = 0
cnt = 0

while adj_list and cnt < marker:
    w, v, e = heappop(adj_list)
    if find_set(v) != find_set(e):
        union(v, e)
        ans += w
        cnt += 1

print(-1 if ans == 0 or cnt != marker - 1 else ans)
