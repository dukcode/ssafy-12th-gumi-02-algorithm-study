def dfs(here):
    vis[here] = True
    for there in range(n):
        if vis[there] or not are_friends[here][there]:
            continue
        dfs(there)


def dfs_all():
    ret = 0
    for idx in range(n):
        if vis[idx]:
            continue
        dfs(idx)
        ret += 1

    return ret


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    are_friends = [[False] * n for _ in range(n)]
    vis = [False] * n
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        are_friends[a][b] = are_friends[b][a] = True

    print(f"#{tc} {dfs_all()}")
