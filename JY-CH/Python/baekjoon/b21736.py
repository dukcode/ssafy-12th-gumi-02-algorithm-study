# 헌내기는 친구가 필요해

import sys
input = sys.stdin.readline
from collections import deque

# 상 하 좌 우

DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)


n, m = map(int, input().split())

data = [list(map(str, input().strip())) for _ in range(n)]

def make_friend(n, m, data):

    for i in range(n):
        for j in range(m):
            if data[i][j] == 'I':
                start_y = i
                start_x = j
            

    
    queue = deque()
    queue.append((start_y, start_x))
    visited = [[0] * m for _ in range(n)]
    visited[start_y][start_x] = 1

    friend = 0
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y + DY[k]
            nx = x + DX[k]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and data[ny][nx] != 'X':
                visited[ny][nx] = 1
                queue.append((ny, nx))
                if data[ny][nx] == 'P':
                    friend += 1
            
    return friend


result = make_friend(n, m, data)
print('TT' if result == 0 else result)