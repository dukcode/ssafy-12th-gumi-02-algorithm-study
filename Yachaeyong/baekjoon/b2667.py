# 단지번호붙이기
from collections import deque


def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    house_cnt = 1
    houses[sr][sc] = 0

    while q:
        cr, cc = q.popleft()

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and houses[nr][nc]:
                house_cnt += 1
                houses[nr][nc] = 0
                q.append((nr, nc))
    return house_cnt


N = int(input())
houses = [list(map(int, input().strip())) for _ in range(N)]
area_cnt = 0

ans = []
for i in range(N):
    for j in range(N):
        if houses[i][j]:
            ans.append(bfs(i, j))
            area_cnt += 1

ans.sort()
print(area_cnt)
for i in range(area_cnt):
    print(ans[i])