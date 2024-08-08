t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())

    adj = [[] for _ in range(v)]
    for _ in range(e):
        fr, to = map(lambda x: int(x) - 1, input().split())
        adj[fr].append(to)

    st, en = map(lambda x: int(x) - 1, input().split())

    def connected(st, en):
        vis = [False] * v

        stk = [st]
        vis[st] = True
        while stk:
            here = stk.pop()

            if here == en:
                return 1

            for there in adj[here]:
                if vis[there]:
                    continue

                vis[there] = True
                stk.append(there)

        return 0

    print(f"#{tc} {connected(st, en)}")
