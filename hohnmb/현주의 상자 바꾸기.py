T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())    
 
    arr = [0] * (N+1)
 
 
    for i in range(Q):  
        L, R = map(int, input().split()) 
        for j in range(L, R+1):
            arr[j] = i+1
    arr.pop(0)
    print(f'#{tc}', end=' ')
    print(*arr)