n = int(input())

COINS = (500, 100, 50, 10)
count = 0


for coin in COINS:
    count += n // coin
    n %= coin

print(count)
