# 최소 생산 비용
MX = 987_654_321


def solve(product, cost):
    global min_cost

    if product == n:
        min_cost = min(min_cost, cost)
        return

    if cost >= min_cost:
        return

    for factory in range(n):
        if taken[factory]:
            continue
        taken[factory] = True
        solve(product + 1, cost + arr[product][factory])
        taken[factory] = False


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    taken = [False] * n
    min_cost = MX

    solve(0, 0)

    print(f"#{tc} {min_cost}")
