# 노드의 거리
from collections import deque


def bfs():
    discovered = [False] * v

    q = deque()

    q.append((s, 0))
    discovered[s] = True

    while q:
        here, dist = q.popleft()

        if here == g:
            return dist

        for there in range(v):
            if not adj[here][there]:
                continue

            if discovered[there]:
                continue

            discovered[there] = True
            q.append((there, dist + 1))

    return 0


t = int(input())
for tc in range(1, t + 1):
    v, e = map(int, input().split())

    adj = [[False] * v for _ in range(v)]
    for _ in range(e):
        fr, to = map(lambda x: int(x) - 1, input().split())
        adj[fr][to] = True
        adj[to][fr] = True

    s, g = map(lambda x: int(x) - 1, input().split())

    print(f"#{tc} {bfs()}")
