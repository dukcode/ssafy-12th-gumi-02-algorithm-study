# s11315 오목 판정

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    board = [input() for _ in range(N)]

    result = 'NO'
    for r in range(N):
        for c in range(N):
            for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                nr, nc = r, c
                cnt = 0
                while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 'YES'
                    nr, nc = nr + dr, nc + dc

    print(f'#{tc} {result}')
