# 우주선 착륙
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]

    # 우 하 좌 상 우상 우하 좌하 자상
    dr = [0, 1, 0, -1, -1, 1, 1, -1]
    dc = [1, 0, -1, 0, 1, 1, -1, -1]


    landing_count = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i + dr[k]
                nj = j + dc[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if land[i][j] > land[ni][nj]:
                        cnt += 1
            if cnt >= 4:
                landing_count += 1

    print(f'#{tc} {landing_count}')