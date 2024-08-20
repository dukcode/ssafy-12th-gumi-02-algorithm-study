# 7576 토마토
from collections import deque
# 열 행
M, N = map(int, input().split())
tom = [list(map(int, input().split())) for _ in range(N)]

days = 0
q = deque()

# 익은 토마토 좌표 저장
for i in range(N):
    for j in range(M):
        if tom[i][j] == 1:
            q.append([i, j])

# 1: 익은 토마토 0: 안 익은 토마토 -1 : 빈칸
def bfs():
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and not tom[nr][nc]:
                q.append([nr, nc])
                tom[nr][nc] = tom[cr][cc] + 1

bfs()

for row in tom:
    for t in row:
        if t == 0:
            print(-1)
            exit()
    else:
        days = max(days, max(row))

print(days-1)