# 바닥 공사

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
for idx in range(3, n+1):
    dp[idx] = (dp[idx - 1] + 2 * dp[idx - 2]) % 796796

print(dp[n])