# 노드의 거리

# bfs 정의합니다.
# 시작 정점과 마지막 정점을 받습니다.
def bfs(S, G):
    visited = [0] * (V+1) # visited 생성
    q = [] # q 생성
    q.append(S) # 시작점 인큐
    visited[S] = 1 # 인큐 했으니까 방문 표시
    while q:    # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0) # 디큐
        for w in range(1, V + 1):  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0 and num_lst[t][w] == 1:
                q.append(w)  # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1
    if not visited[G]:
        return 0
    else:
        return visited[G] - 1





T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    num_lst = [[0] * (V+1) for _ in range(V+1)]
    for k in range(E):
        i, j = map(int, input().split())
        num_lst[i][j] = 1
        num_lst[j][i] = 1
    S, G = map(int, input().split())
    result = bfs(S, G)
    print(f'#{tc} {result}')

