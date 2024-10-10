# 예산
N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start = 0
end = max(budget)
ans = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for b in budget:
        if b > mid:
            temp += mid
        else:
            temp += b

    if temp <= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
