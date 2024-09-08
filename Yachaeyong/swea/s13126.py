def solve(r, now_sum):
    global min_sum
    if r == N:
        if min_sum > now_sum:
            min_sum = now_sum
            return

    for c in range(N):
        if not check_col[c] and now_sum + cost[r][c] < min_sum:
            now_sum += cost[r][c]
            check_col[c] = 1
            solve(r + 1, now_sum)
            now_sum -= cost[r][c]
            check_col[c] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    check_col = [0] * N
    min_sum = 99 * N
    solve(0, 0)
    print(f'#{tc} {min_sum}')
