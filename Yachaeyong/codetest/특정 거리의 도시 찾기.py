from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)


def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1] * (N + 1)
    visited[start] = 0

    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[now] + 1

    ret = []
    for i in range(1, N + 1):
        if visited[i] == K:
            ret.append(i)

    return ret

ans = bfs(X)
if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)
