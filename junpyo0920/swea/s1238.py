from collections import deque


def bfs(start):
    ret = 0
    tmp_list = []

    queue = deque([(start, 0)])
    visited = [False] * 101
    visited[start] = True
    while queue:
        cur_node, cnt = queue.popleft()
        if cnt > ret:
            ret = cnt
            tmp_list = [cur_node]
        if cnt == ret:
            tmp_list.append(cur_node)

        for i in range(101):
            if adj_mat[cur_node][i] and not visited[i]:
                visited[i] = True
                queue.append((i, cnt + 1))

    return tmp_list


for tc in range(1, 11):
    n, s = map(int, input().split())
    data = list(map(int, input().split()))

    adj_mat = [[0] * 101 for _ in range(101)]

    for i in range(0, n, 2):
        adj_mat[data[i]][data[i + 1]] = 1

    print(f"#{tc} {max(bfs(s))}")
