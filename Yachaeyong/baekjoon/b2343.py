# 기타 레슨

N, M = map(int, input().split())
video = list(map(int, input().split()))

st = max(video)
en = sum(video)

ans = 0
while st <= en:
    mid = (st + en) // 2
    cnt = 1
    temp = 0
    for v in video:
        if temp + v > mid:
            cnt += 1
            temp = 0
        temp += v

    if cnt <= M:
        ans = mid
        en = mid - 1
    else:
        st = mid + 1

print(ans)
