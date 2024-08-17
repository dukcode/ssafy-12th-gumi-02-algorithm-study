T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[-1] * N for _ in range(N)]

    # 초기 설정
    B = 1
    W = 2
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2][N // 2] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B

    for _ in range(M):
        r, c, stone = map(int, input().split())
        board[r - 1][c - 1] = stone

        # 놓은 돌에 인접한 모든 방향 확인
        for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            nr = r + dr - 1
            nc = c + dc - 1
            # 놓은 돌에 인접한 +2도 체크
            flip = []
            while 0 <= nr < N and 0 <= nc < N and board[nr][nc] != stone and board[nr][nc] != -1:
                flip.append((nr, nc))
                nr += dr
                nc += dc

            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == stone:
                for fr, fc in flip:
                    board[fr][fc] = stone

    cnt_black = 0
    cnt_white = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_black += 1
            elif board[i][j] == 2:
                cnt_white += 1

    print(f'#{tc} {cnt_black} {cnt_white}')
