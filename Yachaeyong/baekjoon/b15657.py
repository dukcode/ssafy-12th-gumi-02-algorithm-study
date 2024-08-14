# N과 M (8)

N, M = map(int, input().split())
num = list(map(int, input().split()))
result = []
# num.sort()

min_idx = 0
for i in range(N):
    min_idx = i
    for j in range(i+1, N):
        if num[min_idx] > num[j]:
            min_idx = j
    num[i], num[min_idx] = num[min_idx], num[i]

def dfs(st):
    if len(result) == M:
        print(*result)
        return
    for i in range(st, N):
        result.append(num[i])
        dfs(i)  # 중복도 가능함. 중복 뺄려면 i+1하면 됨
        result.pop()

dfs(0)