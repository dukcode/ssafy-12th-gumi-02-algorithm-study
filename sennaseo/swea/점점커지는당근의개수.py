T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
 
    cnt = 1
    result = 1
    for i in range(1, N):
        if C[i-1] < C[i]:
            cnt += 1
            if result < cnt:
                result = cnt
        else:
            cnt = 1
 
    print(f'#{tc} {result}')