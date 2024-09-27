N = int(input())

foods = list(map(int, input().split()))
dp = [0] * 101

dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + foods[i])

print(dp[N - 1])
