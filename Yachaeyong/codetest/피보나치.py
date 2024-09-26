# # 1. 재귀(탑다운)
# # 메모이제이션용 list
# dp = [0] * 100
#
#
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if dp[n]:
#         return dp[n]
#     dp[n] = fibo(n - 2) + fibo(n - 1)
#
#     return dp[n]
#
# print(fibo(99))

# 2. 반복문(바텀업)

dp = [0] * 100

dp[1] = 1
dp[2] = 1
n = 99

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])