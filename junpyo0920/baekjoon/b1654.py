def get_line_count(length):
    ret = 0
    for line in arr:
        ret += line // length
    return ret


k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
shortest = max(arr)

s = 1
e = shortest

while s <= e:
    mid = (s + e) // 2
    cnt = get_line_count(mid)

    if cnt < n:
        e = mid - 1
    else:
        s = mid + 1

print(e)
