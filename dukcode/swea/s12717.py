from collections import deque

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))

    for _ in range(m):
        q.append(q.popleft())

    print(f"#{tc} {q[0]}")
