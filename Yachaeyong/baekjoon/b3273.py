# 두 수의 합

import sys

N = int(input())
num = list(map(int, sys.stdin.readline().split()))
X = int(input())

num.sort()

start = 0
end = N - 1

cnt = 0
while start < end:
    now_sum = num[start] + num[end]

    if now_sum > X:
        end -= 1
    elif now_sum < X:
        start += 1
    else:
        cnt += 1
        end -= 1
        start += 1

print(cnt)
