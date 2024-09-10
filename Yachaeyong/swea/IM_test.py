def solve(cr, cc):
    wall = 0
    for r in range(N):
        for c in range(N):
            if data[r][c] == 1:
                wall += 1
    visible = 0
    for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        for k in range(1, N):
            nr, nc = cr + dr * k, cc + dc * k
            if 0 <= nr < N and 0 <= nc < N:
                if data[nr][nc] == 0:
                    visible += 1
                elif data[nr][nc] == 1:
                    break

    return N * N - wall - visible + 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                ans = solve(r, c)

    print(f'#{tc} {ans}')