# 길 찾기


# 0번 정점에서 시작해서 99번에 도착할 수 있으면, 1 아니면 0을 반환하는 함수
# dfs 수행하면서 99번 정점에 도착하면 1반환

def dfs():
    start, end = 0, 99
    stack = [start]
    # 경로 지정을 위해서 stack
    visited = [0] * 100
    visited[start] = 1
    # 재방문 방지를 위해서 visited
    # stack의 마지막 요소가 현재 위치
    # 현재 위치에서 갈 수 있는 정점 찾으면서
    # 갈 수 있는 정점이 있으면 경로에 추가, 없으면 현재정점 제거
    while stack:
        current = stack[-1]
        if current == end: # 현재 위치가 찾는 목적지라면
            return 1    # 1반환
        # 아직 목적지가 아니라면 길찾기 계속하기
        # 현재 정점과 연결된 정점 보기 >> graph[0][current], graph[1][current]
        for i in range(2):
            v = graph[i][current] # 방문하려는 정점번호
            if v != -1 and not visited[v]: # 정점에 방문하지 않았으면 방문
                stack.append(v)
                visited[v] = 1
                break
        else: #현재 정점에서 갈 수 있는 길이 없음!
            stack.pop() # 현재 정점을 경로상에서 제거
    return 0


for _ in range(10):
    tc, E = map(int, input().split())
    # 그래프 저장하기
    graph = [[-1] * 100 for _ in range(2)]
    data = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        # graph의 0번에 다른 정점 정보가 있으면 1번에 넣기
        # date[i], data[i+1] : data[i]에서 data[i+1] 번으로 갈 수 있다.
        if graph[0][data[i]] == -1:
            graph[0][data[i]] = data[i+1]
        else:
            graph[1][data[i]] = data[i+1]

   result = dfs()