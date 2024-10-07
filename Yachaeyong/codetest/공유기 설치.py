N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort()

# 최소 인접 거리
start = 1
# 최대 인접 거리
end = house[-1] - house[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    value = house[0]
    cnt = 1

    for i in range(1, N):
        if house[i] >= value + mid:
            value = house[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)