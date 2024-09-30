n = int(input())
dp = [0] * int((1e6 + 1))

for i in range(2, n + 1):
    temp_dis = dp[i - 1] + 1

    if i % 2 == 0:
        temp_dis = min(temp_dis, dp[i // 2] + 1)
    if i % 3 == 0:
        temp_dis = min(temp_dis, dp[i // 3] + 1)
    dp[i] = temp_dis

print(dp[n])
