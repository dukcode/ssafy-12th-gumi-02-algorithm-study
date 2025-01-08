# 그림
def bfs(fr, fc):
    queue = []
    queue.append([fr,fc])
    visited[fr][fc] = 1
    a = 1

   
    while queue:
        sr, sc = queue.pop(0)

        for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
            nr, nc = sr + dr, sc + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc]:
                queue.append([nr,nc])
                visited[nr][nc] = 1
                a += 1


    return a

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]




area = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt += 1
            area = max(bfs(i,j), area)

print(cnt)
print(area)
