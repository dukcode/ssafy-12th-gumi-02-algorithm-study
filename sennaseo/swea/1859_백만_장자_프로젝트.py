def solve():
    money = 0
    start = 0
    while start < N:
        max_idx = start
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
    result = solve()
    print(f"#{tc} {result}")
