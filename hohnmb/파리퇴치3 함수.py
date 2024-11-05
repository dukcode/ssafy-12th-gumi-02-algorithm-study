d_1 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

d_2 = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

T = int(input())

for tc in range(1,T+1):
    N,M = list(map(int,input().split()))
    arr =  [list(map(int,input().split())) for _ in range(N)]
    
    def kill_sum(r,c,delta):
        S = arr[r,c]

        for dr,dc in delta:
            for i in range(1,M):
                nr, nc = r + dr*i, c + dc*i
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    break
                S += arr[nr][nc]
        return S
    ans = 0
    for r in range(N):
        for c in range(N):
            ans = max(ans,kill_sum(r,c,d_1))
            ans = max(ans,kill_sum(r,c,d_2))
    print(f'#{tc} {ans}')