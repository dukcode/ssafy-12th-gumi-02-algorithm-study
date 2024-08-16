T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flower = 0
    min_flower = 9 * (N * 2 - 1)

    for r in range(N):
        for c in range(N):
            flower = 0
            for k in range(1, N+1):
                for dr, dc in [[0, k], [k, 0], [0, -k], [-k, 0]]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        flower += arr[nr][nc]
            flower += arr[r][c]
            if max_flower < flower:
                max_flower = flower
            if min_flower > flower:
                min_flower = flower

    print(f'#{tc} {max_flower - min_flower}')
