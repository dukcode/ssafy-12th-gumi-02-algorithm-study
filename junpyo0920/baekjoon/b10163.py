N = int(input())
mat = [[0] * 1001 for _ in range(1001)]

for i in range(1, N+1):
    x1, y1, w, h = map(int, input().split())
    for y in range(y1, y1+h):
        for x in range(x1, x1+w):
            mat[y][x] = i

for num in range(1, N+1):
    ans = 0
    for y in range(1001):
        ans += mat[y].count(num)
    print(ans)
