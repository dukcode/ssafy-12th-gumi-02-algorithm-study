# 벽 부수고 이동하기

import sys
input = sys.stdin.readline
from pprint import pprint as pp
from collections import deque

# 상 하 좌 우
DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)


def find_road(n, m, data):
    
    # 3차원은 생각도 못했네;;;
    # y, x, crush
    # 시작점
    queue = deque([(0, 0, 0)])
    # 벽을 안부셨을때의 거리, 벽을 부셨을때의 거리를 방문 배열에 기록
    visited = [[[0, 0] for _ in range(m) ]for _ in range(n)]
    # 시작점 일단 1 올려주고
    visited[0][0][0] = 1
    while queue:
        y, x, crush = queue.popleft()
        
        # 도착하면 종료
        if y == n-1 and x == m-1:
            return visited[y][x][crush]

        for k in range(4):
            ny = y + DY[k]
            nx = x + DX[k]
            
            if 0 <= ny < n and 0 <= nx < m:
                # 벽이 있고 벽 부순적 없음
                if data[ny][nx] == '1' and crush == 0:
                    # 벽을 부셔서 뚫은것 = 벽부시기전에서 + 1이다
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    # 이때부턴 벽 못부수게 crush 1
                    # 이후로 기록되는 값들은 방문 배열중 벽을 부시고 도착한 거리를 기록한다.
                    queue.append((ny, nx, 1))
                # 벽이 없고 방문 안함
                elif data[ny][nx] == '0' and visited[ny][nx][crush] == 0:
                    visited[ny][nx][crush] = visited[y][x][crush] + 1
                    # 이 부분들은 벽을 안 부시고 도착한 거리를 기록한다.
                    queue.append((ny, nx, crush))
    
    return -1

n, m = map(int, input().split())
data = [list(input().strip()) for _ in range(n)]
print(find_road(n, m, data))