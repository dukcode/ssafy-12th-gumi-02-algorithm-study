# 효율적인 화폐 구성

n, m = map(int, input().split())

money = []
for i in range(n):
    money.append(int(input()))

dp = [10001] * (m + 1)

#... 실패..

