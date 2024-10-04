# LIS : 가장 긴 증가하는 부분 수열

N = int(input())

attack = list(map(int, input().split()))
attack.reverse()

# dp[i] = attack[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if attack[j] < attack[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
