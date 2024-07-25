from collections import deque

MX = 987_654_321


n, m = map(int, input().split())
are_friends = [[False] * n for _ in range(n)]


for _ in range(m):
    a, b = map(lambda i: int(i) - 1, input().split())
    are_friends[a][b] = True
    are_friends[b][a] = True

min_val = MX
ans = -1
for i in range(n):
    visited = [False] * n
    q = deque()
    q.append((i, 0))
    visited[i] = True
    bacon = 0
    while q:
        cur, dist = q.popleft()
        for next in range(n):
            if visited[next]:
                continue

            if not are_friends[cur][next]:
                continue

            q.append((next, dist + 1))
            visited[next] = True
            bacon += dist + 1

    if bacon < min_val:
        min_val = min(min_val, bacon)
        ans = i

print(ans + 1)
