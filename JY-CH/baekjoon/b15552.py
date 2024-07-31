# 빠른 A + B

import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


# input() 과 sys.stdin.readline() 차이

# 둘다 값을 받는 것은 동일함
# 그러나 반복문에서 너무 많은 값을 받아서 돌릴경우 시간초과 발생
# 이를 방지하고자 반복문에서 여러 줄을 받을때는
# sys.stdin.readline()을 사용한다