T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    biggest_pang = 0
    smallest_pang = 1000000
    for i in range(N):
        for j in range(N):
            max_pang = arr[i][j]
            for k in range(4):
                for l in range(1, N+1):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        max_pang += arr[ni][nj]
            if biggest_pang < max_pang:
                biggest_pang = max_pang
    for i in range(N):
        for j in range(N):
            min_pang = arr[i][j]
            for k in range(4):
                for l in range(1, N+1):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l
                    if 0 <= ni < N and 0 <= nj < N:
                        min_pang += arr[ni][nj]
            if smallest_pang > min_pang:
                smallest_pang = min_pang
    print(f'#{tc} {biggest_pang - smallest_pang}')