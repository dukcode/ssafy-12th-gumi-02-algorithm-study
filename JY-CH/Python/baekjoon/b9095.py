# 1,2,3 더하기

t = int(input())

for case in range(t):
    n = int(input())
    dp = [0] * 101

    for idx in range(1, n + 1):
        if idx == 1:
            dp[idx] = 1
        elif idx == 2:
            dp[idx] = 2
        elif idx == 3:
            dp[idx] = 4
        else:
            dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx - 3]

    print(dp[n])



