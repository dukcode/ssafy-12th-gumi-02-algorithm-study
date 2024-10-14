def dfs(V, S, G):
    visited = [0] * (V + 1)
    stack = []
    visited[S] = 1
    stack.append(S)
    v = S

    while True:
        for w in node_lst[v]:
            if visited[w] == 0:
                if w == G:
                    return 1
                stack.append(w)
                visited[w] = 1
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return 0


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    node_lst = [[] for _ in range(V + 1)]
    lst = [list(map(int, input().split())) for _ in range(E)]

    S, G = map(int, input().split())

    for i in range(E):
        V1, V2 = lst[i][0], lst[i][1]
        node_lst[V1].append(V2)
    print(f"#{tc} {dfs(V, S, G)}")
