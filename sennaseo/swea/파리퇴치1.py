T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for x in range(N)]
    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            for k in range(M):
                for l in range(M):
                    fly_sum += arr[i+k][j+l]
            if max_num < fly_sum:
                max_num = fly_sum
    print(f'#{tc} {max_num}')