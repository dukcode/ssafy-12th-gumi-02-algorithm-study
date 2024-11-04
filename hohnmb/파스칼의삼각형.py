T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            if j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
            print(arr[i][j],end=' ')
        print()