dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def dfs(sy, sx):
    ret = 1
    visited[sy][sx] = 1
    stack = [(sy, sx)]
    while stack:
        cy, cx = stack[-1]
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < h and 0 <= nx < w and data[ny][nx] and not visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = 1
                ret += 1
                break
        else:
            stack.pop()
    return ret


h, w = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]
visited = [[0] * w for _ in range(h)]
cnt = 0
size = 0
for y in range(h):
    for x in range(w):
        if data[y][x] and not visited[y][x]:
            cnt += 1
            size = max(size, dfs(y, x))
print(cnt)
print(size)
