T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    max_pang = 0
    for i in range(N):
        for j in range(M):
            balloon_pang = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    balloon_pang += arr[ni][nj]
            if max_pang < balloon_pang:
                max_pang = balloon_pang
    print(f'#{tc} {max_pang}')
