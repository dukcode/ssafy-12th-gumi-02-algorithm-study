for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    ans = arr[0][0] + arr[0][1] + arr[1][0]
    for y in range(n):
        for x in range(m):
            temp = arr[y][x]
            for i in range(4):
                if 0 <= y + dy[i] < n and 0 <= x + dx[i] < m:
                    temp += arr[y + dy[i]][x + dx[i]]
            ans = temp if ans < temp else ans

    print(f'#{tc + 1} {ans}')