T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    da = [-1, 1, 0, 0]
    db = [0, 0, -1, 1]
    dc = [-1, 1, -1, 1]
    dd = [1, 1, -1, -1]
    max_kill = 0
    for a in range(N):
        for b in range(N):
            kill_line = arr[a][b]
            kill_x = arr[a][b]
            for c in range(4):
                for d in range(1, M):
                    ni = a + da[c] * d
                    nj = b + db[c] * d
                    if 0 <= ni < N and 0 <= nj < N:
                        kill_line += arr[ni][nj]
                    nk = a + dc[c] * d
                    nl = b + dd[c] * d
                    if 0 <= nk < N and 0 <= nl < N:
                        kill_x += arr[nk][nl]
            if max_kill < kill_line:
                max_kill = kill_line
            if max_kill < kill_x:
                max_kill = kill_x
    print(f'#{tc} {max_kill}')