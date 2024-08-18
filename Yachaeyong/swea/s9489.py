# 9489. 고대 유적

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for r in range(N):
        for c in range(M):
            for dr, dc in [[0, 1], [1, 0]]:
                cnt = 0
                if arr[r][c]:
                    cnt += 1
                nr, nc = r + dr, c + dc
                while 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                    cnt += 1
                    nr += dr
                    nc += dc
                max_v = max(cnt, max_v)

    print(f'#{tc} {max_v}')
