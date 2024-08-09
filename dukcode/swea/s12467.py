MX = 987_654_321
t = int(input())


for tc in range(1, t + 1):
    # n : 정류장의 총 갯수
    # k : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # m : 충전기의 갯수
    # arr : 충전기의 위치
    k, n, m = map(int, input().split())

    arr = list(map(int, input().split()))

    chargers = [False] * (n + 1)
    for i in arr:
        chargers[i] = True

    cache = [[-1] * (k + 1) for _ in range(n + 1)]

    def can_arrive(pos, battery, cnt):
        if pos == n:
            return cnt

        if cache[pos][battery] != -1:
            return cache[pos][battery]

        ret = MX
        if battery != 0:
            ret = can_arrive(pos + 1, battery - 1, cnt)

        if chargers[pos]:
            ret = min(ret, can_arrive(pos + 1, k - 1, cnt + 1))

        cache[pos][battery] = ret
        return ret

    ans = can_arrive(0, k, 0)

    if ans == MX:
        ans = 0

    print(f"#{tc} {ans}")
