# 2일차 - 전자카트
MX = 987_654_321


def get_min_energy(here, taken, cnt):
    if cnt == n:
        return consumptions[here][0]

    ret = MX
    for there in range(n):
        if taken[there]:
            continue

        taken[there] = True
        ret = min(
            ret, get_min_energy(there, taken, cnt + 1) + consumptions[here][there]
        )
        taken[there] = False

    return ret


def solve():
    taken = [False] * n
    taken[0] = True
    return get_min_energy(0, taken, 1)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    consumptions = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{tc} {solve()}")
