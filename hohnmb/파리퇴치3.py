di = [0,1,0,-1]
dj = [1,0,-1,0]

mi = [-1,1,1,-1]
mj = [1,1,-1,-1]


T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_kill = 0
    for i in range(n):
        for j in range(n):
            start_1 = start_2 = arr[i][j]
            for k in range(4):
                for l in range(1,m):
                    ni = i + di[k]*l
                    nj = j + dj[k]*l

                    xi = i + mi[k]*l
                    xj = j + mj[k]*l
                    if 0 <= ni < n and 0 <= nj < n:
                        start_1 += arr[ni][nj]
                    if 0 <= xi < n and 0 <= xj < n:
                        start_2 += arr[xi][xj]
                if max_kill < start_1:
                    max_kill = start_1
                if max_kill < start_2:
                    max_kill = start_2
    print(f'#{tc} {max_kill}')


