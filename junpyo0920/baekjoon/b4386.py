from heapq import heappush, heappop
from math import sqrt


def prim(start):
    hq = [(0.0, start)]
    u = set()

    total_cost = 0.0
    while hq:
        cur_cost, cur_pos = heappop(hq)

        if cur_pos not in u:
            u.add(cur_pos)
            total_cost += cur_cost

            for i in range(n):
                if stars[i] != cur_pos and stars[i] not in u:
                    new_cost = sqrt(sum(map(lambda x: (x[0]-x[1]) ** 2, zip(cur_pos, stars[i]))))
                    heappush(hq, (new_cost, stars[i]))

    print(total_cost)


n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
prim(stars[0])
