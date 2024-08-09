# 최댓값

arr = [list(map(int, input().split())) for _ in range(9)]

max_v = 0
max_i, max_j = 0, 0

for i in range(9):
    for j in range(9):
        if max_v < arr[i][j]:
            max_v = arr[i][j]
            max_i, max_j = i, j

print(max_v)
print(max_i+1, max_j+1) # 문제는 1~9행렬이라서 +1