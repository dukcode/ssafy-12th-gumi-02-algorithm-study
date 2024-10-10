# 7 2
# 1 1 2 2 2 2 3
# 7 4
# 1 1 2 2 2 2 3
def get_start_idx_of(s, e, t):
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] < t:
            s = mid + 1
            continue

        e = mid - 1
    return s


def get_last_idx_of(s, e, t):
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] <= t:
            s = mid + 1
            continue

        e = mid - 1
    return e


n, target = map(int, input().split())
arr = list(map(int, input().split()))

s_idx = get_start_idx_of(0, n - 1, target)
e_idx = get_last_idx_of(0, n - 1, target)

cnt = e_idx - s_idx + 1
print(cnt if cnt else -1)
