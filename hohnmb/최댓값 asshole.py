arr = [list(map(int,input().split())) for _ in range(9)]


max_value = 0
idx = []
for i in range(9):
    for j in range(9):
        if  max_value < arr[i][j]:
            max_value = arr[i][j]



for i in range(9):
    for j in range(9):
        if arr[i][j] == max_value:
            idx.append(i+1)
            idx.append(j+1)

print(max_value)
print(*idx)
