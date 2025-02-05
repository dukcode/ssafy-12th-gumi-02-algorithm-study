from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()

stack = deque([])

for _ in range(int(input())):
    command_list = input().split()
    command = command_list[0]
    item = command_list[-1]
    stack_size = len(stack)

    if command == "push":
        stack.append(int(item))
    elif command == "pop":
        print(stack.pop() if stack_size else -1)
    elif command == "size":
        print(stack_size)
    elif command == "empty":
        print(int(stack_size == 0))
    elif command == "top":
        print(stack[-1] if stack_size else - 1)
