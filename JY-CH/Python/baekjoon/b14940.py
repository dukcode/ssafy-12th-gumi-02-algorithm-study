# 쉬운 최단거리

import sys
input = sys.stdin.readline
from collections import deque

# 상 하 좌 우
DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)

def find_road(n, m, data, check):
    # 시작점 탐색
    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                y, x = i, j

    # 시작점 기반 bfs 시작
    queue = deque()
    queue.append((y, x))
    check[y][x] = 0
    while queue:
        y, x = queue.popleft()
        
        # 델타
        for k in range(4):
            ny = y + DY[k]
            nx = x + DX[k]
            
            # ny, nx 범위 / data[ny][nx] 가 갈 수 있는땅, check[ny][nx]가 가본적이 없는 곳
            if 0 <= ny < n and 0 <= nx < m and data[ny][nx] == 1 and check[ny][nx] == -1:
                check[ny][nx] = check[y][x] + 1
                queue.append((ny, nx))

    # 마지막에 data[i][j]가 벽(0)인 부분 초기화
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                check[i][j] = 0
    return check


n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

# 이건 좀 참신했다.
# 못가는 부분을 어떻게 표현할지를 고민했는데
# 그냥 시작을 -1로 잡고 돌리면 결국 닿지 못하는 부분은 그대로 남으니까
# -1로 남길 수 있다.
check = [[-1] * m for _ in range(n)]
result = find_road(n, m, data, check)

# print(data)
for i in range(n):
    print(*result[i])


