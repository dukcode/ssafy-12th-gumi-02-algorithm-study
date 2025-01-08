# 파스칼의 삼각형

def solve (r, arr):
    if r == N:
        return

    for j in range(r + 1):
        if j == 0:
            arr[r][j] = 1
        else:
            arr[r][j] = arr[r-1][j] + arr[r-1][j-1]
    solve(r+1, arr)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    solve(0, arr)
    print(f'#{tc}')
    for i in range(N):
        for j in range(i + 1):
            print(arr[i][j], end=' ')
        print()

