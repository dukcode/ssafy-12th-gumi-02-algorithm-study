# 카드2
from collections import deque

N = int(input())

q = deque(i for i in range(1, N + 1))
while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
