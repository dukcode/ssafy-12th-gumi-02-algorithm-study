# 미로의 거리
from collections import deque

WALL = 1
START = 2
END = 3

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)


def find(board, value):
    for y in range(n):
        for x in range(n):
            if board[y][x] == value:
                return (y, x)


def bfs():
    discovered = [[False] * n for _ in range(n)]

    q = deque()

    q.append((st, 0))
    discovered[st[0]][st[1]] = True

    while q:
        cur, cur_dist = q.popleft()

        for dir in range(4):
            ny = cur[0] + dy[dir]
            nx = cur[1] + dx[dir]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if board[ny][nx] == WALL:
                continue

            if discovered[ny][nx]:
                continue

            if board[ny][nx] == END:
                return cur_dist

            discovered[ny][nx] = True
            q.append(((ny, nx), cur_dist + 1))

    return 0


# 미로의 거리
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    st = find(board, START)
    print(f"#{tc} {bfs()}")
