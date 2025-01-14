# 피보나치 함수


import sys
input = sys.stdin.readline

def fibo(x):

    dp = [0, 0] * (41)
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, 41):
        dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]
    
    if x == 0:
        return dp[0]
    elif x == 1:
        return dp[1]
    else:
        return dp[x]

n = int(input())


for _ in range(n):
    x = int(input())
    print(*fibo(x))