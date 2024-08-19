da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]
dc = [-1, 1, -1, 1]
dd = [1, 1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    max_value = 0
    for a in range(N):
        for b in range(N):
            k1 = arr[a][b]
            k2 = arr[a][b]
            for c in range(4):
                for d in range(1, M):
                    ni = a + da[c] * d
                    nj = b + db[c] * d
                    if 0 <= ni < N and 0 <= nj < N:
                        k1 += arr[ni][nj]
                    nk = a + dc[c] * d
                    nl = b + dd[c] * d
                    if 0 <= nk < N and 0 <= nl < N:
                        k2 += arr[nk][nl]
            if max_value < k1:
                max_value = k1
            if max_value < k2:
                max_value = k2
    print(f'#{tc} {max_value}')
