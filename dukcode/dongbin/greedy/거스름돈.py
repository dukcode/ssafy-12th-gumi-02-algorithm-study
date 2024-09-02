COINS = (500, 100, 50, 10)

n = int(input())
cnt = 0

for coin in COINS:
    if n // coin == 0:
        continue

    cnt += n // coin
    n %= coin

print(cnt)
