
T = int(input())  
 
for tc in range(1, T+1):  

    N = int(input())  
 

    arr = [list(map(int, input().split())) for _ in range(N)]  # 
 

    arr_90 = [[0 for _ in range(N)] for _ in range(N)]   
    arr_180 = [[0 for _ in range(N)] for _ in range(N)] 
    arr_270 = [[0 for _ in range(N)] for _ in range(N)]  
 
    for i in range(N):  
        for j in range(N):  
            arr_90[i][j] = arr[N-1-j][i] 
 
    for i in range(N):  
        for j in range(N): 
            arr_180[i][j] = arr_90[N-1-j][i] 
 
    for i in range(N):  
        for j in range(N):  
            arr_270[i][j] = arr_180[N-1-j][i]  
 
    print('#{}'.format(tc))  
    for i in range(N):  
        for a in range(N):  
            print(arr_90[i][a], end='')  
        print(end=' ')  
         
        for b in range(N):
            print(arr_180[i][b], end='')  #
        print(end=' ')  
 
        for c in range(N):
            print(arr_270[i][c], end='')  
        print()   