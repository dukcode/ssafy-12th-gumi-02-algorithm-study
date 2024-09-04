n = int(input())
moves_direction = list(map(str, input().split()))
x, y = 1, 1

DIRECT = ["L", "R", "U", "D"]
DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

for move in moves_direction:
    for i in range(len(DIRECT)):
        if move == DIRECT[i]:
            nx = x + DX[i]
            ny = y + DY[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
