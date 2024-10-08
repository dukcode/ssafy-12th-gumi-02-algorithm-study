N, M = map(int, input().split())
rice_cake = list(map(int, input().split()))

start = 0
end = max(rice_cake)

ans = 0
while start <= end:
    mid = (start + end) // 2
    temp = 0
    for rice in rice_cake:
        if rice > mid:
            temp += (rice - mid)

    if temp < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
print(ans)
