from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    called = [0] * 101
    called[start] = 1
    max_cnt = -1
    max_node = 0

    while q:
        now_node, now_cnt = q.popleft()
        if max_cnt < now_cnt:
            max_cnt = now_cnt
            max_node = now_node
        if max_cnt == now_cnt:
            max_node = max(max_node, now_node)

        for next_node in graph[now_node]:
            if called[next_node]:
                continue

            called[next_node] = 1
            q.append((next_node, now_cnt + 1))

    return max_node


for tc in range(1, 10 + 1):
    data_len, start_node = map(int, input().split())
    data = list(map(int, input().split()))

    graph = [[] for _ in range(101)]

    for i in range(0, data_len, 2):
        if data[i + 1] not in graph[data[i]]:
            graph[data[i]].append(data[i + 1])

    print(f'#{tc} {bfs(start_node)}')
