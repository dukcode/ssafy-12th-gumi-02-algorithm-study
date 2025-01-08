# 괄호
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    data = list(input().strip())

    stack = []
    result = 'YES'
    for word in data:
        if word == '(':
            stack.append(word)
        else:
            if len(stack) == 0:
                result = 'NO'
                break
            stack.pop()
    if len(stack):
        result = 'NO'

    print(result)