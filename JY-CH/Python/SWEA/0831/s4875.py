# 미로

# def dfs(sy, sx):
#     stack = [(sy, sx)]
#     visited = [[0] * N for _ in range(N)]
#     visited[sy][sx] = 1
#     dy = [0, 1, 0, -1]
#     dx = [1, 0, -1, 0]
#     while stack:
#         y1, x1 = stack[-1]
#         if maze[y1][x1] == 3:
#             return 1
#         for k in range(4):
#             ny, nx = y1 + dy[k], x1 + dx[k]
#             if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and maze[ny][nx] != 1:
#                 stack.append((ny, nx))
#                 visited[ny][nx] = 1
#                 break
#         else:
#             stack.pop()
#     return 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#     y, x = 0, 0
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:
#                 y, x = i, j
#     result = dfs(y, x)
#     print(f'#{tc} {result}')



def dfs(sr, sc):
    stack = [(sr, sc)]
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while stack:
        r, c = stack[-1]
        if maze[r][c] == 3:
            return 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not \
                    visited[nr][nc] and maze[nr][nc] != 1:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()

    return 0


def start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return dfs(i,j)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    result = start()
    print(f'#{tc} {result}')

