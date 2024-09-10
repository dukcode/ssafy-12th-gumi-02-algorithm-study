T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                for k in range(4):
                    for l in range(N):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 0:
                                arr[ni][nj] = 1
                            elif arr[ni][nj] == 1:
                                break
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    print(f"#{tc} {cnt}")
