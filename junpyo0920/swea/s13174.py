def find_set(x):
    if p[x] == x:
        return x

    return find_set(p[x])


def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if a != b:
        p[b] = a


for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    p = [x for x in range(n+1)]

    for i in range(0, m * 2, 2):
        union(data[i], data[i + 1])

    representative = set()

    for i in range(1, n + 1):
        representative.add(find_set(i))

    print(f"#{tc+1} {len(representative)}")
