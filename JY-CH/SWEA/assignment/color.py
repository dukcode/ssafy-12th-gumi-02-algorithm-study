# 색칠하기

t = int(input())
for tc in range(1, t+1):
    arr = [[0] * 10 for _ in range(10)]
    n = int(input())

    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if arr[x][y]:
                    if arr[x][y] != color:
                        arr[x][y] = 3

                else :
                    arr[x][y] = color

    cnt = 0
    for x in range(10):
        for y in range(10):
            if arr[x][y] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')

