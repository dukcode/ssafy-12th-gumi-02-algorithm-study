# 그래프 경로
from pprint import pprint

def dfs(S, G):
    # 시작 포인트를 스택에.
    stack = [S]
    # 방문체크용 리스트 하나 만들고
    visited = [0] * (V+1)

    while stack:
        top = stack[-1]
        if top == G:
            return 1

        for i in link[top]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

    return 0





T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    link = [[] for _ in range (V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        # 링크 인덱스 a 자리의 리스트에 b를 어펜드
        link[a].append(b)

    S, G = map(int, input().split())
    result = dfs(S, G)

    print(f'#{tc} {result}')