# 대표값2

n = 5
lst = []
for i in range(n):
    lst.append(int(input()))

lst_sum = 0
for j in range(n):
    lst_sum += lst[j]

lst_ave = int(lst_sum / n)

lst.sort()


middle = 0
middle += lst[n//2]

print(lst_ave)
print(middle)


