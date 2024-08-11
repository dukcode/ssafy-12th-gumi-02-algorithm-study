# dfs, bfs >>> '그래프'를 순회하는 방법
E = 8
v = 7
# 인접행렬
adj = [[0] * (v+1) for _ in range(v+1)]
data = list(map(int, input().split()))
for i in range(0, E*2, 2):
    a = data[i]
    b = data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
for row in adj:
    print(row)

# s: dfs 를 수행하려고 하는 시작 정점 번호
def dfs(s):
    # 경로를 저장할 stack
    # 재방문을 방지하기 위해서 visited
    stack = [s] # 시작 정점을 포함하는 경로
    visited = [8] * (v+1) # v번 인덱스까지 필요하니까...
    visited[s] = 1 # 시작 정점은 이미 방문했음을 표시
    # stack이 비어있지 않으면 반복 >>> 탐샐할 정점이 남아 있으면 반복
    while stack:    # 아래 작업을 반복, 언제까지? 더 이상 탐색할 경로가 없을때까지 계속해서 반복
    # 현재 정점에서 인접한 정점 탐색
    current = stack[-1]
    # 현재 정점과 인접한 정점정보는 어디에 있습니까?    adj[current]
    for i in range(1,v+1):
       # adj[current][i] >>> 1이면 current와 i가 인접한 정점
        # 만약에 인접하면서, 방문하지 않았으면 방문
        # 방문하게 되면, 경로에 추가, 방문 표시 하기
        if adj[current][i] and not visited[i] == 0:
            stack.append(i)
            visited[i] = 1
            break   # current에 인접한 정점 찾기 중단

   else: # current 정점에서 갈 수 있는 정점이 없다