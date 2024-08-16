T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for r in range(N):
        for c in range(N):
            sum_cross = arr[r][c]
            for i in range(1, M):
                for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nr = r + dr * i
                    nc = c + dc * i
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_cross += arr[nr][nc]

            sum_x = arr[r][c]
            for j in range(1, M):
                for dr, dc in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:
                    nr = r + dr * j
                    nc = c + dc * j
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_x += arr[nr][nc]

            kill = max(sum_cross, sum_x)
            if max_v < kill:
                max_v = kill

    print(f'#{tc} {max_v}')
