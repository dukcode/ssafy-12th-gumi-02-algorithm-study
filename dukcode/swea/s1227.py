# 미로2
from collections import deque

T = 10
N = 100

WALL = 1
START = 2
END = 3

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)


def find(board, target):
    for y in range(N):
        for x in range(N):
            if board[y][x] == target:
                return (y, x)


def dfs():
    discovered = [[False] * N for _ in range(N)]

    q = deque()

    q.append(start)
    discovered[start[0]][start[1]] = True

    while q:
        cur = q.popleft()

        if board[cur[0]][cur[1]] == END:
            return 1

        for dir in range(4):
            ny = cur[0] + dy[dir]
            nx = cur[1] + dx[dir]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if discovered[ny][nx]:
                continue

            if board[ny][nx] == 1:
                continue

            discovered[ny][nx] = True
            q.append((ny, nx))

    return 0


for _ in range(T):
    tc = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    start = find(board, START)

    print(f"#{tc} {dfs()}")
