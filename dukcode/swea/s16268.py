import sys

sys.stdin = open("input.txt", "r")

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

t = int(input())


def calcScore(y, x):
    score = board[y][x]

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue

        score += board[ny][nx]

    return score


for tc in range(1, t + 1):
    h, w = tuple(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(h)]

    ans = -1

    for y in range(h):
        for x in range(w):
            ans = max(ans, calcScore(y, x))

    print(f"#{tc} {ans}")
