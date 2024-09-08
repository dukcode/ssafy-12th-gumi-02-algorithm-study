def solve2():
    max_v = data[-1]
    money = 0
    for i in range(N - 1, -1, -1):
        if data[i] <= max_v:
            money += max_v - data[i]
        else:
            max_v = data[i]
    return money


def solve():
    money = 0
    start = 0
    while start < N:
        max_idx = start  #
        for i in range(start, N):
            if data[i] >= data[max_idx]:
                max_idx = i
        for i in range(start, max_idx):
            money += data[max_idx] - data[i]
        start = max_idx + 1
    return money


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    result = solve2()
    print(f"#{tc} {result}")
