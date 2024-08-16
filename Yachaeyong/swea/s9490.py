T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flower = 0
    for r in range(N):
        for c in range(M):
            flower = 0
            n = arr[r][c]
            for n in range(1, n+1):
                for dr, dc in [[0, n], [n, 0], [0, -n], [-n, 0]]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M:
                        flower += arr[nr][nc]
            flower += arr[r][c]
            if max_flower < flower:
                max_flower = flower

    print(f'#{tc} {max_flower}')