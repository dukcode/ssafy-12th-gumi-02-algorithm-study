import sys
sys.setrecursionlimit(100000)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def search_safe_area(rain, y, x):
    visited[y][x] = 1
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and area[ny][nx] - rain > 0:
            search_safe_area(rain, ny, nx)
    else:
        return


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
rain_counts = [0] * 10001

for y in range(N):
    for x in range(N):
        rain_counts[area[y][x]] += 1

ans = 1
for idx in range(10001):
    if rain_counts[idx]:
        safe_area = 0
        visited = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if area[y][x] - idx > 0 and not visited[y][x]:
                    safe_area += 1
                    search_safe_area(idx, y, x)
        if ans < safe_area:
            ans = safe_area

print(ans)
