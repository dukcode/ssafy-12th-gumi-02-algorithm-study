T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    goldmine = [[0] * M for _ in range(N)]
    i = 0
    for r in range(N):
        for c in range(M):
            goldmine[r][c] = data[i]
            i += 1

    for c in range(1, M):
        for r in range(N):
            if r == 0:
                left_up = 0
            else:
                left_up = goldmine[r - 1][c - 1]
            if r == N - 1:
                left_down = 0
            else:
                left_down = goldmine[r + 1][c - 1]

            left = goldmine[r][c - 1]

            goldmine[r][c] += max(left, left_up, left_down)

    ans = 0
    for i in range(N):
        ans = max(ans, goldmine[i][M - 1])

    print(ans)
