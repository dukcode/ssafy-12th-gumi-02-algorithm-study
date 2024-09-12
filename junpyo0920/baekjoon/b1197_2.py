def find_set(x):
    if p[x] == x:
        return x

    p[x] = find_set(p[x])
    return find_set(p[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if root_x < root_y:
        p[root_y] = root_x
    else:
        p[root_x] = root_y


v, e = map(int, input().split())
edges = [() for _ in range(e)]
p = [x for x in range(v + 1)]

for i in range(e):
    s, e, w = map(int, input().split())
    edges[i] = (w, s, e)
edges.sort()

sum_w = 0
cnt = 0
for (w, s, e) in edges:
    if find_set(s) != find_set(e):
        cnt += 1
        union(s, e)
        sum_w += w

        if cnt == v - 1:
            break

print(sum_w)
