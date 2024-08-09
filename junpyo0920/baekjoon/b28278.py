# https://www.acmicpc.net/problem/28278
# 스택 구현 해보기

# for문 안에서 input()으로 받았더니 시간초과,
# sys.stdin.readline()으로 해결
import sys

N = int(input())
stack = [None] * N
top = -1

for _ in range(N):
    func = list(map(int, sys.stdin.readline().strip().split()))
    if func[0] == 1:
        top += 1
        stack[top] = func[1]
    elif func[0] == 2:
        if top != -1:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    elif func[0] == 3:
        print(top + 1)
    elif func[0] == 4:
        if top != -1:
            print(0)
        else:
            print(1)
    elif func[0] == 5:
        if top != -1:
            print(stack[top])
        else:
            print(-1)
