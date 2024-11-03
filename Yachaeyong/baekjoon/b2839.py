# 설탕 배달

N = int(input())
# 1. 그리디
cnt = 0
while N >= 0:
    if N % 5 == 0:
        cnt += N //5
        print(cnt)
        break
    cnt += 1
    N -= 3
else:
    print(-1)

# # 2. dp
# INF = int(1e9)
# dp = [INF] * 5001
#
# dp[3] = dp[5] = 1
# for i in range(6, N + 1):
#     dp[i] = min(dp[i - 3], dp[i - 5]) + 1
#
# print(dp[N] if dp[N] < INF else -1)
