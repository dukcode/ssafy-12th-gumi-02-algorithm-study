
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        for k in range(1, j+1):
            if i-k < 0 or i+k >= N:
                break
            if arr[i-k] == arr[i+k]:
                arr[i-k] = arr[i+k] = (arr[i-k]+1) % 2
 
    print(f'#{tc}', *arr)