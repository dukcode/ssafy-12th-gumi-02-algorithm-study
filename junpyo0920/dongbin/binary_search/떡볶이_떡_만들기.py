def get_sliced_tteok_len(slice_size):
    ret = 0

    for tteok in tteoks:
        ret += tteok - slice_size if tteok - slice_size > 0 else 0

    return ret


tteok_cnt, request_len = map(int, input().split())
tteoks = sorted(list(map(int, input().split())))

s = 0
e = tteoks[-1]

while s <= e:
    mid = (s + e) // 2
    sliced_tteok_len = get_sliced_tteok_len(mid)

    if sliced_tteok_len < request_len:
        e = mid - 1
    else:
        s = mid + 1

print(e)
