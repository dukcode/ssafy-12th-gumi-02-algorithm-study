n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_price = min(prices)

now = 0
oil = 0
cost = 0
while now < n - 1:
    if prices[now] == min_price:
        remain_distances = 0
        for i in range(now, n - 1):
            remain_distances += distances[i]
        cost += (remain_distances - oil) * min_price
        break

    if oil < distances[now]:
        remain_distances = 0
        for next in range(now, n - 1):
            if prices[now] > prices[next]:
                break
            remain_distances += distances[next]
        cost += (remain_distances - oil) * prices[now]
        oil += remain_distances - oil

    oil -= distances[now]
    now += 1

print(cost)