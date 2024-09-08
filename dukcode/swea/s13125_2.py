# 전기버스2 - DP (Bottom Up) 풀이
MX = 987_654_321


def solve():
    cache = [MX] * n

    cache[0] = 0
    for here in range(0, n - 1):
        for there in range(here + 1, here + arr[here] + 1):
            if there > n - 1:
                continue

            cache[there] = min(cache[there], cache[here] + 1)

    return cache[n - 1] - 1


t = int(input())
for tc in range(1, t + 1):
    n, *arr = list(map(int, input().split()))

    print(f"#{tc} {solve()}")
