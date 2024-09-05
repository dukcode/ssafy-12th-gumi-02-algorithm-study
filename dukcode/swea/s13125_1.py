# 전기버스2 - DP (Top Down) 풀이
MX = 987_654_321


def get_min_cnt():
    return solve(n - 1) - 1


def solve(now):
    if now == 0:
        return 0

    if cache[now] != -1:
        return cache[now]

    ret = MX
    for before in range(0, now):
        if before + arr[before] < now:
            continue

        ret = min(ret, solve(before) + 1)

    cache[now] = ret
    return ret


t = int(input())
for tc in range(1, t + 1):
    n, *arr = list(map(int, input().split()))

    cache = [-1] * (n + 1)
    print(f"#{tc} {get_min_cnt()}")
