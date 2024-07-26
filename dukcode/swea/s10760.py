dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (1, 1, 0, -1, -1, -1, 0, 1)

t = int(input())

for tc in range(1, t + 1):
    h, w = tuple(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(0, h)]

    ans = 0
    for y in range(h):
        for x in range(w):
            cnt = 0
            for dir in range(8):
                ny = y + dy[dir]
                nx = x + dx[dir]

                if ny < 0 or ny >= h or nx < 0 or nx >= w:
                    continue

                if board[ny][nx] < board[y][x]:
                    cnt += 1

            if cnt >= 4:
                ans += 1

    print(f"#{tc} {ans}")
