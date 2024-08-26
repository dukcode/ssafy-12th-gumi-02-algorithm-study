# 28278 스택2

import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == '1':
        stack.append(order[1])
    elif order[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)