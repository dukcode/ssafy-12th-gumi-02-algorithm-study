T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [list(map(int, input().split())) for x in range(N)]
    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]
    max_num = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if ground[ni][nj] < ground[i][j]:
                        cnt += 1
            if cnt >= 4:
                max_num += 1
    print(f'#{tc} {max_num}')