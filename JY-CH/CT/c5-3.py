# 음료수 얼려먹기
# 재귀

def dfs(y, x):
    # 이탈할경우 False, 아니라면 True.
    if y <= -1 or y >= n or x <= -1 or x >= m:
        return False
    if arr[y][x] == 0:
        arr[y][x] = 1
        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y + 1, x)
        dfs(y, x + 1)
        return True
    return False





m = 3
n = 3
arr = [list(map(int, input())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1
print(result)






