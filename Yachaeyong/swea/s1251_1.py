from heapq import heappush, heappop

def prim():
    heapq = [(0, 0)]
    used = [0] * N
    pay_sum = 0

    while heapq:
        now_pay, now_island = heappop(heapq)

        if used[now_island]:
            continue

        used[now_island] = 1
        pay_sum += now_pay

        for next_island, next_pay in island[now_island]:
            if used[next_island]:
                continue

            heappush(heapq, (next_pay, next_island))

    return round((pay_sum))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    island = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            pay = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) * E
            island[i].append((j, pay))

    print(f'#{tc} {prim()}')
