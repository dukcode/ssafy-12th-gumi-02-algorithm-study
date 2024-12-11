# 스택
import sys
input = sys.stdin.readline


n = int(input())
stack = []
for data in range(n):
    data = input().split()

    if data[0] == 'push':
        stack.append(data[1])

    elif data[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            # 이래도 된다.
            # stack.pop은
            # 1번 스택의 마지막 요소를 '제거'하고
            # 2번 그 요소를 반환하기 때문이다.
            print(stack.pop())

    elif data[0] == 'size':
        print(len(stack))

    elif data[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)

    elif data[0] == 'top':
        if len(stack) == 0:
            print(-1)
        elif len(stack) == 1:
            print(stack[0])
        else:
            print(stack[-1])