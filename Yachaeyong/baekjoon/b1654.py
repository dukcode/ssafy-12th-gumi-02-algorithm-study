# 랜선 자르기
K, N = map(int, input().split())
wlan_cable = [int(input()) for _ in range(K)]
# wlan_cable.sort()

start = 1
# end = wlan_cable[-1]
end = max(wlan_cable)
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for w in wlan_cable:
        cnt += (w // mid)

    if cnt >= N:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
