def solve():
    ret = 0
    sell_price = -1
    for price in prices[::-1]:
        sell_price = max(sell_price, price)
        ret += sell_price - price

    return ret


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    prices = list(map(int, input().split()))
    print(f"#{tc} {solve()}")
