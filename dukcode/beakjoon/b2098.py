MX = 987_654_321
n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
cache = [[-1] * (1 << n) for _ in range(n)]


start = 0


def solve(here, vis):
    if vis == ((1 << n) - 1):
        if adj[here][start] != 0:
            return adj[here][start]
        return MX

    if cache[here][vis] != -1:
        return cache[here][vis]

    ret = MX
    for there in range(n):
        if (vis & (1 << there)) or adj[here][there] == 0:
            continue
        ret = min(ret, solve(there, vis | (1 << there)) + adj[here][there])

    cache[here][vis] = ret
    return ret


print(solve(start, 1 << start))
