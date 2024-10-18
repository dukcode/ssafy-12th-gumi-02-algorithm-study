INF = int(1e9)
n = int(input())
m = int(input())

adj_mat = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    adj_mat[i][i] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    adj_mat[a][b] = min(adj_mat[a][b], w)

for stopover in range(1, n + 1):
    for a in range(1, n + 1):
        if stopover == a:
            continue
        for b in range(1, n + 1):
            if a == b:
                continue
            adj_mat[a][b] = min(adj_mat[a][b], adj_mat[a][stopover] + adj_mat[stopover][b])

for y in range(1, n + 1):
    for x in range(1, n + 1):
        print(adj_mat[y][x] if adj_mat[y][x] != INF else 0, end=" ")
    print()
