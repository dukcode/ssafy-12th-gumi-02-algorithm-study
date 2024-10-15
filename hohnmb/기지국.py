T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    home_cnt = 0
    gz_home_cnt = 0
    position = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    gz_dict = {'A': 1,'B': 2,'C': 3}
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                home_cnt += 1
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                for d in range(4):
                    for l in range(1,gz_dict[arr[i][j]]+1):
                        r = i+dr[d]*l
                        c = j+dc[d]*l
                        if 0<=r<N and 0<=c<N:
                            if arr[r][c] == 'H' and [r,c] not in position:
                                position.append([r,c])
                                gz_home_cnt += 1
    result = home_cnt - gz_home_cnt
    print(f"#{tc} {result}")