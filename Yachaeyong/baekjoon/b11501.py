# 주식
T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = price[-1]
    gain = 0
    for i in range(N - 1, -1, -1):
        if price[i] < max_price:
            gain += max_price - price[i]
        else:
            max_price = price[i]

    print(gain)
