# 색종이

num = int(input())
n = 100
m = 10
arr = [[0] * n for _ in range(n)]

for _ in range(num):

    px, py = map(int, input().split())

    for x in range(px, px + m):
        for y in range(py, py + m):
            arr[x][y] = 1


cnt = 0
for x in range(n):
    for y in range(n):
        cnt += arr[x][y]

print(cnt)
