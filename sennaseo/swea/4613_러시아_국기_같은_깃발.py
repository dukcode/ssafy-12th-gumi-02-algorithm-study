def solve():
    min_v = N * M
    for i in range(1, N - 1):
        for j in range(i, N - 1):
            count = coloring(i, j)
            if count < min_v:
                min_v = count
    return min_v


def coloring(b1, b2):
    cnt = 0
    for W1 in range(0, b1):
        for W2 in range(M):
            if flag[W1][W2] != "W":
                cnt += 1

    for B1 in range(b1, b2 + 1):
        for B2 in range(M):
            if flag[B1][B2] != "B":
                cnt += 1

    for R1 in range(b2 + 1, N):
        for R2 in range(M):
            if flag[R1][R2] != "R":
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    result = solve()
    print(f"#{tc} {result}")
