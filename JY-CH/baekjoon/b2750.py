# 수 정렬하기

n = int(input())
n_lst = []
for _ in range(5):
    num = int(input())
    n_lst.append(num)

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if n_lst[j] > n_lst[j+1]:
            n_lst[j], n_lst[j+1] = n_lst[j+1], n_lst[j]

for i in range(n):
    print(n_lst[i])