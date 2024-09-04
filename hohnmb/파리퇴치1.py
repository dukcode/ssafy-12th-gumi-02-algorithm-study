T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    max_kill = 0
    for i in range(n):
        for j in range(n):
            kill_sum = 0
            for k in range(m):
                for l in range(m):
                    if 0<= i+k < n and 0 <= j+l < n:
                        kill_sum += arr[i+k][j+l]

            if max_kill < kill_sum:
                max_kill = kill_sum

    print(f'#{tc} {max_kill}')