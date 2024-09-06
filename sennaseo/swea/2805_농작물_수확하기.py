T = int(input())
for tc in range(1, T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
 
    x = 0
    y = n // 2
 
    dx, dy = [[1, 1, -1, -1], [-1, 1, 1, -1]]
    get = farm[x][y]
 
    farm[x][y] = -1
 
    for i in range(n//2+1):
        for j in range(4):
            for k in range(i, n//2):
                nx = x + dx[j]
                ny = y + dy[j]
                x, y = nx, ny
                if farm[x][y] == -1:
                    break
                get += farm[x][y]
                farm[x][y] = -1
 
        x += 1
        if x < n and farm[x][y] != -1:
            get += farm[x][y]
            farm[x][y] = -1
 
    print(f'#{tc} {get}')