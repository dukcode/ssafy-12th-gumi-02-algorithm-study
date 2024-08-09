T = 10
N = 100
A = 0
B = 99

for tc in range(1, T + 1):
    _, n = map(int, input().split())

    adj = [[-1] * N for _ in range(2)]
    edges = list(map(int, input().split()))
    for i in range(0, 2 * n, 2):
        fr = edges[i]
        to = edges[i + 1]

        if adj[0][fr] != -1:
            adj[1][fr] = to
        else:
            adj[0][fr] = to

    def dfs(st, en):
        vis = [False] * N

        stk = [st]
        vis[st] = True
        while stk:
            here = stk.pop()

            if here == en:
                return 1

            for next in (adj[0][here], adj[1][here]):
                if next == -1:
                    continue

                if vis[next]:
                    continue

                vis[next] = True
                stk.append(next)

        return 0

    print(f"#{tc} {dfs(A, B)}")
