for tc in range(int(input())):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0

    for y in range(n):
        blanks = 0
        for x in range(n):
            if arr[y][x]:
                blanks += 1
                if x == n - 1 and blanks == k:
                    cnt += 1
                    blanks = 0
            else:
                if blanks == k:
                    cnt += 1
                blanks = 0

    for x in range(n):
        blanks = 0
        for y in range(n):
            if arr[y][x]:
                blanks += 1
                if y == n - 1 and blanks == k:
                    cnt += 1
                    blanks = 0
            else:
                if blanks == k:
                    cnt += 1
                blanks = 0
    
    print(f'#{tc + 1} {cnt}')