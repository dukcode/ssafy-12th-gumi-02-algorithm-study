def solve(r, now_probaility):
    global max_success
    if r == N:
        max_success = max(max_success, now_probaility)
        return
    if now_probaility <= max_success:
        return

    for c in range(N):
        if not taken[c]:
            taken[c] = 1
            solve(r + 1, now_probaility * probability[r][c])
            taken[c] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    probability = [list(map(lambda i:int(i)/100, input().split())) for _ in range(N)]
    taken = [0] * N
    max_success = 0
    solve(0, 1)
    print(f'#{tc} {max_success * 100:.6f}')
