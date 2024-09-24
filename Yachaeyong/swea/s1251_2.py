def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    island = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            distance = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
            island.append((i, j, distance))

    island.sort(key=lambda x: x[2])

    parent = [i for i in range(N)]
    cnt = 0
    min_dist = 0
    for s, e, dist in island:
        if find(s) != find(e):
            union(s, e)
            cnt += 1
            min_dist += dist

            if cnt == N - 1:
                break

    print(f'#{tc} {round(min_dist * E)}')
