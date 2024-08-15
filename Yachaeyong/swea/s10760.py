T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    candidates = 0

    for r in range(N):
        for c in range(M):
            can = 0
            for dr, dc in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and land[r][c] > land[nr][nc]:
                    can += 1
            if can >= 4:
                candidates += 1

    print(f'#{tc} {candidates}')
