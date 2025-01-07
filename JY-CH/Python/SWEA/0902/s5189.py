# 전자 카트

def solve(idx):
    global min_v
    if idx == N-1:
        path = [0] + perm + [0]

        total = 0
        for i in range(N):
            total += data[path[i]][path[i+1]]
        if total < min_v:
            min_v = total
        return

    for i in range(1, N):
        if not check[i]:
            perm[idx] = i
            check[i] = 1
            solve(idx+1)
            check[i] = 0







T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    perm = [0] * (N-1)
    check = [0] * N
    min_v = 99999999999
    solve(0)
    print(f'#{tc}c {min_v}')