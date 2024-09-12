from heapq import heappush, heappop


def prim(start):
    h = [(0, start)]
    u = [0] * (v + 1)

    sum_w = 0
    while h:
        w, now = heappop(h)

        if not u[now]:
            u[now] = 1
            sum_w += w
            for i in range(len(adj_list[now])):
                next, next_w = adj_list[now][i]
                if not u[next]:
                    heappush(h, (next_w, next))

    print(sum_w)


v, e = map(int, input().split())
adj_list = [[] for _ in range(v + 1)]

for _ in range(e):
    s, e, w = map(int, input().split())
    adj_list[s].append((e, w))
    adj_list[e].append((s, w))

prim(1)
