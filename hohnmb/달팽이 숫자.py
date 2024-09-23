T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]

    dx = [0, 1, 0, -1] 
    dy = [1, 0, -1, 0]
    dir = 0
    r, c = 0, 0

    for num in range(1, N*N+1):

        arr[r][c] = num

        r += dx[dir]
        c += dy[dir]

        if r < 0 or r >= N or c < 0 or c >= N or arr[r][c]:

            r -= dx[dir]
            c -= dy[dir]

            dir = (dir + 1) % 4

            r += dx[dir]
            c += dy[dir]

    print('#' + str(tc))
    for row in arr:
        print(*row)