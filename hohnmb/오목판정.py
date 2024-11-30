
di = [0, 1, 0, -1]  
dj = [1, 0, -1, 0]
 

di2 = [-1, 1, 1, -1]
dj2 = [1, 1, -1, -1]
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
 
    ok = False
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    count = 1
                    for l in range(1,5):
                        ni = i + di[k]*l
                        nj = j + dj[k]*l
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                            count += 1
 
                        if count >= 5:
                            ok = True
                            break
 
            if arr[i][j] == 'o':
                for k in range(4):
                    count = 1
                    for l in range(1, 5):
                        ni2 = i + di2[k] * l
                        nj2 = j + dj2[k] * l
                        if 0 <= ni2 < N and 0 <= nj2 < N and arr[ni2][nj2] == 'o':
                            count += 1
 
                        if count >= 5:
                            ok = True
                            break
 
            if ok == True:
                break
        if ok == True:
            break
 
    if ok == True:
        print(f'#{tc} {"YES"}')
    else:
        print(f'#{tc} {"NO"}')