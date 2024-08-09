for tc in range(int(input())):
    N, Q = map(int, input().split())
    ans = ['0'] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for idx in range(L - 1, R):
            ans[idx]  = str(i)
    print(f'#{tc + 1} {" ".join(ans)}')