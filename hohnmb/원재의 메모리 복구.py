T = int(input())
 
for tc in range(1, T + 1):
    N = list(map(int,input()))
 
    count = 0
    prev = 0  
    for i in range(len(N)):
        if N[i] != prev:  
            count += 1
            prev = N[i] 
 
    print(f'#{tc} {count}')