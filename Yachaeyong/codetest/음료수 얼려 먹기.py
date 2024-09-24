'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''

from collections import deque

N, M = map(int, input().split())

ice = [list(map(int, input())) for _ in range(N)]


def bfs(sr, sc):
    q = deque([(sr, sc)])
    ice[sr][sc] = 1

    while q:
        cr, cc = q.popleft()
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and not ice[nr][nc]:
                q.append((nr, nc))
                ice[nr][nc] = 1


ans = 0
for r in range(N):
    for c in range(M):
        if ice[r][c] == 0:
            bfs(r, c)
            ans += 1

print(ans)
