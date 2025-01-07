# 길찾기 그래프 2안

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

        #  graph[current] >> 연결된 정점 정보를 가지는 리스트
        is_find = False
        for v in graph[current]:
            if not visited[v]:
                stack.append(v)
                visited[v] = 1
                is_find = True
                break
                
        if not is_find:
            stack.pop()




graph = [[] * for _ in range(100)]
data = list(map(int, input().split()))
for i in range(0, E*2, 2):
    #date[i], data[i+1]
    graph[data[i]].append(data[i+1])
