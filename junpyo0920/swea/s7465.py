def find_set(x):
    if p[x] == x:
        return x

    return find_set(p[x])


def union(x, y):
    a = find_set(x)
    b = find_set(y)

    if a < b:
        p[a] = b
    else:
        p[b] = a


for tc in range(int(input())):
    n, m = map(int, input().split())
    p = [x for x in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    representative = set(p)

    print(f"#{tc+1} {len(representative)- 1}")
