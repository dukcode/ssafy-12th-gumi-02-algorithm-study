# 계단 오르기

import sys
input = sys.stdin.readline

n = int(input())

stair = []
for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0] + stair[1])
else:
    dp = [0] * (n + 1)
    dp[1] = stair[0]
    dp[2] = stair[0] + stair[1]

    for i in range(3, n + 1):
        # 규칙 찾기 빡세다 ㄹㅇ
        # 2계단 전에서 오는 경우, 3계단전에서 2칸 뛰고 건너오는경우
        dp[i] = max(dp[i - 2], dp[i - 3] + stair[i - 2]) + stair[i - 1]
    print(dp[n])