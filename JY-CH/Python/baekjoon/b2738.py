# 행렬 덧셈

n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    c = list(map(int, input().split()))
    a.append(c)

for i in range(n):
    d = list(map(int, input().split()))
    b.append(d)


for i in range(n):
    for j in range(m):
        result = a[i][j] + b[i][j]
        print(result, end=' ')
    print()

