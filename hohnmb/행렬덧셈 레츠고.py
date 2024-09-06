n,m = map(int,input().split())

arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]


sum_list = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        sum_list[i][j] += arr1[i][j]

for i in range(n):
    for j in range(m):
        sum_list[i][j] += arr2[i][j]


for x in sum_list:
    print(*x)


