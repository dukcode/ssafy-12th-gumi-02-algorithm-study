def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return find_set(parents[x])


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if heights[root_x] < heights[root_y]:
            parents[root_x] = root_y
            heights[root_y] += 1
        else:
            parents[root_y] = root_x
            heights[root_x] += 1


n, m = map(int, input().split())
parents = [x for x in range(n + 1)]
heights = [0] * (n + 1)

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")