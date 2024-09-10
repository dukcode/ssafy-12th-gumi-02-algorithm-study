def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        if a > b:
            p[a] = b
        else:
            p[b] = a


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]

    want = list(map(int, input().split()))
    for i in range(0, len(want), 2):
        f = want[i]
        s = want[i + 1]
        union(f, s)
    #
    for i in range(1, N+1):
        find(i)

    print(f'#{tc} {len(set(p)) - 1}')