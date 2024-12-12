# 큐
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
queue = deque()
for data in range(n):
    data = input().split()

    if data[0] == 'push':
        queue.append(data[1])

    elif data[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            # 이래도 됩니다.
            print(queue.popleft())

    elif data[0] == 'size':
        print(len(queue))

    elif data[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)

    elif data[0] == 'back':
        if len(queue) == 0:
            print(-1)
        elif len(queue) == 1:
            print(queue[0])
        else:
            print(queue[-1])

    elif data[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])