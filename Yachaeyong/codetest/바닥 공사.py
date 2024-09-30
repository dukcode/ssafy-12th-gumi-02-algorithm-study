N = int(input())

dp = [0] * 1001
# 바텀업
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = 2*dp[i-2] + dp[i-1]

print(dp[N] % 796796)

# 탑다운
# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 3
#
#     if dp[n] != 0:
#         return dp[n]
#     dp[n] = 2 * f(n - 2) + f(n - 1)
#     return dp[n]
# print(f(N)%796796)
