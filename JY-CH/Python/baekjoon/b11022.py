# A + B - 8

import sys

t = int(input())

for tc in range(t):
    a, b = map(int, sys.stdin.readline().split())
    add_all = a + b
    print(f'Case #{tc+1}: {a} + {b} = {add_all}')


# 7번이랑 다를건 없고
# f-string 사이에 잘 넣어주면 된당.