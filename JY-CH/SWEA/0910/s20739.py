# 고대 유적2

for tc in range(int(input())):
    n, m = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for y in range(n):
        cnt = 0
        for x in range(m):
            if land[y][x] == 1:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                cnt = 0


    for x in range(m):
        cnt = 0
        for y in range(n):
            if land[y][x] == 1:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                cnt = 0

    if result < 2:
        result = 0


    print(f'#{tc + 1} {result}')
