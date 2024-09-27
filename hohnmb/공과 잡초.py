T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input()))
 
    N = len(arr)
    cnt = 0
 
    for i in range(N):
        if arr[i] == '(' or arr[i] == ')':
            cnt += 1
 
        if arr[i] == '(' and arr[i+1] == ')':
            cnt -= 1
 
    print(f'#{tc} {cnt}')