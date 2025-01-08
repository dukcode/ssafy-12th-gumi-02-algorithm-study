# 토마토

import sys
input = sys.stdin.readline

from collections import deque


# 상 하 좌 우
DY = (-1, 1, 0, 0)
DX = (0, 0, -1, 1)

def zero():
    for line in range(n):
        if 0 in tomato_field[line]:
            return 1
    return 0   
    
def count():
    
    queue = deque()
    for i in range(n):
        for j in range(m):
            if tomato_field[i][j] == 1:
                 queue.append((i, j))
    
    day = 0
    while queue:
        # 이게 핵심이라고 생각함
        # 이거 못하면 익는 날짜 체크가 안됨됨
        for _ in range(len(queue)):
            y, x = queue.popleft()
        

            for k in range(4):
                ny = y + DY[k]
                nx = x + DX[k]

                if 0 <= ny < n and 0 <= nx < m and tomato_field[ny][nx] == 0:
                    tomato_field[ny][nx] = 1
                    queue.append((ny, nx))

        day += 1
    
    # 다 끝났고 0 있으면 못 익는게 있으니까 -1임
    for line in range(n):
        if 0 in tomato_field[line]:
            return -1

    # 하루가 지나서 익어야되는데 첫 시작부터 체크해서 -1 해야함
    return day - 1


m, n = map(int, input().split())

tomato_field = [list(map(int, input().split())) for _ in range(n)]

# 만약 익을 토마토가 없으면 0, 아니면 count()
print(0 if zero() == 0 else count())
