T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    ans = 0

    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:
            ans += 1

    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[c][r]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        if cnt == K:
            ans += 1

    print(f'#{tc} {ans}')
