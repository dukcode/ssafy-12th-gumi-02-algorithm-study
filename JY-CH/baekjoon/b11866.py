# 요세푸스
from collections import deque

# def get(n, arr):


num, kill = map(int, input().split())


data = list(range(1, num + 1))

result = []
queue = deque()
for i in range(1, len(data) + 1):
    queue.append(i)

cnt = 1
while True:
    if len(queue) == 0:
        break

    if cnt == kill:
        result.append(queue.popleft())
        cnt = 0
    else:
        tmp = queue.popleft()
        queue.append(tmp)

    cnt += 1

answer = ', '.join(map(str, result))
print(f'<{answer}>')