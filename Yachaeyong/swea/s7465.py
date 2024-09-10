def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    return p[x]


def union(x, y):
    a = find_set(x)
    b = find_set(y)
    if a > b:
        p[b] = a
    elif b > a:
        p[a] = b


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = [x for x in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    representative = set()
    for i in range(1, N + 1):
        representative.add(find_set(i))

    print(f'#{tc} {len(representative)}')
