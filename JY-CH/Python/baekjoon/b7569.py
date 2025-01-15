# 또마토 (3차원)

import sys
input = sys.stdin.readline

# 위 아래 상 하 좌 우 
DY = (0, 0, -1, 1, 0, 0)
DX = (0, 0, 0, 0, -1, 1)
DZ = (-1, 1, 0, 0, 0, 0)

from collections import deque

m, n, h = map(int, input().split())

tomato_field = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# print(tomato_field)

# 0이 없다? 익을 토마토가 없다
# 그럼 뭐하러 체크함 바로 0
def zero():
    for flow in range(h):
            for line in range(n):
                if 0 in tomato_field[flow][line]:
                    return -1
    return 0


def count():

    queue = deque()

    # i 위, 아래층 j 상, 하 k 좌, 우
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato_field[i][j][k] == 1:
                    queue.append((i, j, k)) 

    day = 0
    while queue:
        for _ in range(len(queue)):
            z, y, x = queue.popleft()

            for direction in range(6):
                nz = z + DZ[direction]
                ny = y + DY[direction]
                nx = x + DX[direction]

                if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and tomato_field[nz][ny][nx] == 0:
                    tomato_field[nz][ny][nx] = 1
                    queue.append((nz, ny, nx))

        day += 1

    for floor in range(h):
        for line in range(n):
            if 0 in tomato_field[floor][line]:
                return -1
                
    return day - 1


print(zero() if zero() == 0 else count())




