# 음료수 얼려먹기
# 스택을 이용해보자.

# 제자리 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(y, x):
    stack = [(y, x)]
    while stack:
        # 스택이니까 후입 선출임. pop 가만히 냅둬야함.
        # 이미 값이 0이고 방문 안했을때 돌리는걸로 걸어놨음 걍 하면 됨.
        # 스택 pop
        sy, sx = stack.pop()
        # 방문자 표시
        visited[sy][sx] = True
        # 4방향 탐색
        for way in range(4):
            ny = sy + dy[way]
            nx = sx + dx[way]
            # 이거 조건 순서도 중요함
            # 일단 범위 설정후
            # 방문자 체크한 다음
            # 배열에서도 0이면
            # 스택에 넣어줌
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and arr[ny][nx] == 0:
                stack.append((ny, nx))
            # 이과정의 목적은 방문자 표시를 통한 0의 군집을 구하기 위함임.
            # 방문자표시가 핵심임. 이를 통해 0 0 0 0 이 아닌 ( 0 0 0 ) ( 0 )임.


m = 3
n = 3
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            dfs(i, j)
            result += 1
print(result)