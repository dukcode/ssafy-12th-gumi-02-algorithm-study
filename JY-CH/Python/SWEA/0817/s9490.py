# 풍선팡



T = int(input())
for tc in range (1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_value = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]

            for k in range(4):
                for l in range(1, arr[i][j]+1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l

                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]

            if max_value < cnt:
                max_value = cnt
    print(f'#{tc} {max_value}')