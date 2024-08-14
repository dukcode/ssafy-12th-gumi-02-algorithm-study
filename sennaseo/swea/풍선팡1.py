T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, 1, -1]
    pang_max = 0
    for i in range(N):
        for j in range(M):
            pang = arr[i][j]
            for k in range(4):
                for l in range(1, arr[i][j]+1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        pang += arr[ni][nj]
            if pang_max < pang:
                pang_max = pang
    print(f'#{tc} {pang_max}')