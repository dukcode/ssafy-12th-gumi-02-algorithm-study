# 파도반 수열

import sys
input = sys.stdin.readline

def dynamic(num):
    dp = [1] * (num + 1)
    for idx in range(3, num + 1):
        dp[idx] = dp[idx - 2] + dp[idx - 3]

    return dp[num - 1]

n = int(input())
for _ in range(n):
    num = int(input())
    print(dynamic(num))






