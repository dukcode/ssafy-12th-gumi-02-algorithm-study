# 재미있는 오셀로 게임.?

def f(i, j, bw, N):
    board[i][j] = bw        # 지정된 돌 놓기
    for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i + di, j + dj
        tmp = []            # 뒤집을 돌의 인덱스를 저장
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:          # 반대색 돌이면
            tmp.append((ni,nj)) # 뒤집을 돌을 저장하고
            ni, nj = ni + di, nj + dj   # 현재 방향으로 계속 이동
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            for p, q in tmp:
                board[p][q] = bw

# 1이면 흑, 2이면 백
B = 1
W = 2
op = [0, 2]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 보드 한변의길이 N, 돌을 놓는 횟수 M
    play = [list(map(int, input().split()))]

    board = [[0] * N for _ in range(N)] # N*N board 준비 , 0 -> N-1 인덱스 사용
    # 중심부 돌을 배치
    # WB
    # BW
    board[N//2-1][N//2-1] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W

    # 돌 놓기
    for col, row, bw in play: # 입력순서 주의, col, row는 1부터 시작, board는 0 부터 시작
        f(row-1, col-1, bw, N)    # 돌놓기, 뒤집기

    bcnt = wcnt = 0     #검은돌 개수, 흰돌 개수
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1
    print(f'#{tc} {bcnt} {wcnt}')