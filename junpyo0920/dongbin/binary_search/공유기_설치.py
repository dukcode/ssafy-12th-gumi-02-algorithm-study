def get_wifi_cnt(distance):
    cnt = 1
    now = 0

    for next in range(now + 1, n):
        if arr[next] >= arr[now] + distance:
            now = next
            cnt += 1

    return cnt


def get_max_distance():
    s = 1
    e = arr[n - 1] - arr[0]

    while s <= e:
        mid = (s + e) // 2
        wifi_cnt = get_wifi_cnt(mid)

        if wifi_cnt < c:
            e = mid - 1
            continue
        s = mid + 1

    return e


n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
max_distance = get_max_distance()
print(max_distance)