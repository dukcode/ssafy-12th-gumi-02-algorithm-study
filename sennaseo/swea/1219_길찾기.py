def dfs():
    start, end = 0, 99
    stack = [start]
    visited = [0] * 100
    visited[start] = 1
    while stack:
        current = stack[-1]
        if current == end:
            return 1
        for i in range(2):
            v = graph[i][current]
            if v != -1 and not visited[v]:
                stack.append(v)
                visited[v] = 1
                break
        else:
            stack.pop()
    return 0


for _ in range(10):
    tc, E = map(int, input().split())
    graph = [[-1] * 100 for _ in range(2)]
    data = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        if graph[0][data[i]] == -1:
            graph[0][data[i]] = data[i + 1]
        else:
            graph[1][data[i]] = data[i + 1]

    result = dfs()
    print(f"#{tc} {result}")
