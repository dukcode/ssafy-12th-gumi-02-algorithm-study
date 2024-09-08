T = int(input())
for tc in range(1, T+1):
    n = int(input())
    map_ = [list(map(str, input())) for _ in range(n)]
 
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]
 
    for i in range(n):
        for j in range(n):
            if map_[i][j] == 'A':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < n and 0 <= nj < n and map_[ni][nj] == 'H':
                        map_[ni][nj] = 'X'
 
            elif map_[i][j] == 'B':
                for k in range(4):
                    for l in range(1, 3):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < n and 0 <= nj < n and map_[ni][nj] == 'H':
                            map_[ni][nj] = 'X'
 
            elif map_[i][j] == 'C':
                for k in range(4):
                    for l in range(1, 4):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < n and 0 <= nj < n and map_[ni][nj] == 'H':
                            map_[ni][nj] = 'X'
 
    count_house = 0
    for i in range(n):
        for j in range(n):
            if map_[i][j] == 'H':
                count_house += 1
    print(f'#{tc} {count_house}')