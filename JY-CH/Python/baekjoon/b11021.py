# A + B - 7

import sys

t = int(input())

for tc in range(t):
    a, b = map(int, sys.stdin.readline().split())
    add_all = a + b
    print(f'Case #{tc+1}: {add_all}')


# sys.stdin.readline() 활용해봄
# swea에서 너무 자주 당한 case number 지정이라 금방 푼듯