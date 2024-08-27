T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
 
    cnt = 0
    for i in range(N): 
        start, end = arr[i]
 
        for j in range(i+1, N):
            if arr[j][1] < end :
                cnt += 1
 
    print(f'#{tc} {cnt}')