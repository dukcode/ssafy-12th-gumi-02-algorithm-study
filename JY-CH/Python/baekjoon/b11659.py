# 구간 합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))


# 이렇게 일찍 풀릴리가 없으니 무조건 터질거라 판단
# 당연히 시간초과
# for _ in range(m):
#     i, j = map(int, input().split())
#     print(sum(data[i-1:j]))


dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i-1] + data[i-1]

for _ in range(m):
    start, end = map(int, input().split())
    print(dp[end] - dp[start - 1])

