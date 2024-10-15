# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

INF = int(1e9)
n, m = map(int, input().split())
adj_mat = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj_mat[a][b] = 1

for layover in range(n + 1):
    for a in range(n + 1):
        if layover == a:
            continue
        for b in range(n + 1):
            if a == b:
                continue
            adj_mat[a][b] = min(adj_mat[a][b], adj_mat[a][layover] + adj_mat[layover][b])

cnt = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if adj_mat[a][b] >= INF and adj_mat[b][a] >= INF and a != b:
            break
    else:
        cnt += 1

print(cnt)
