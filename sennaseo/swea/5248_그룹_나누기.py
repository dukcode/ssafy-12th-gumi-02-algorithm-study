def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx == ry:
        return

    if rx < ry:
        p[rx] = ry
    else:
        p[ry] = rx


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = [x for x in range(N + 1)]
    data = list(map(int, input().split()))
    for i in range(0, M * 2, 2):
        union(data[i], data[i + 1])

    groups = set()
    for i in range(1, N + 1):
        groups.add(find_set(i))

    print(f"#{tc} {len(groups)}")
