T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    ans = 0  
    s, e = N // 2, N // 2
    for i in range(N):
        for j in range(s, e+1):
            ans += a[i][j]
        if i < N // 2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f'#{tc} {ans}')