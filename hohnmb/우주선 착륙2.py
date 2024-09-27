di = [0,1,1,1,0,-1,-1,-1]
dj = [-1,-1,0,1,1,1,0,-1]
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    point = 0
 
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i+di[k]
                nj = j+dj[k]
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] < arr[i][j]:
                    cnt +=1
 
            if cnt >=4:
                point +=1
 
    print(f'#{tc+1} {point}')