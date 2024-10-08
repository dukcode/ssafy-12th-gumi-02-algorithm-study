# 공유기 설치
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

start = 1
end = house[-1]-house[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    post_house = house[0]
    for i in range(1, N):
        # 직전에 공유기 설치한 집 위치 갱신
        if house[i] >= mid + post_house:
            post_house = house[i]
            cnt += 1

    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)