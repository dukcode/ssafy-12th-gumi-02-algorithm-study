di = [0,1,0,-1]
dj = [1,0,-1,0]
 
 
 
T = int(input())
 
for tc in range(1,T+1):
    n,m = map(int,input().split())
    f_powder = [list(map(int,input().split())) for _ in range(n)]
    max_value = 0
    for i in range(n):
        for j in range(m):
            start = f_powder[i][j]
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    start += f_powder[ni][nj]
            if start > max_value:
                max_value = start
 
    print(f'#{tc} {max_value}')