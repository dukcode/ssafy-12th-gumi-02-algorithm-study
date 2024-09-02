N = int(input())
road = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
ans = 0
for i in range(N - 1):
    if min_price > prices[i]:
        min_price = prices[i]

    ans += (min_price * road[i])


print(ans)
