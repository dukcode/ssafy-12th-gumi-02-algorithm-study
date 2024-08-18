mat = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            mat[y][x] = 1

ans = 0
for y in range(101):
    for x in range(101):
        if mat[y][x]:
            ans += 1

print(ans)