def solve(a, b):
    if ground[a][b] < ground_average:
        ground[a][b] += 1
        return 1 + solve(a, b)
    elif ground[a][b] > ground_average:
        ground[a][b] -= 1
        return 1 + solve(a, b)
    elif ground[a][b] == ground_average:
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1, c1, r2, c2 = map(int,input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    ground_sum = 0
    ground_cnt = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            ground_sum += ground[i][j]
            ground_cnt += 1

    ground_average = ground_sum//ground_cnt
    cnt = 0

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            cnt += solve(i,j)

    print(f'#{tc} {cnt}')