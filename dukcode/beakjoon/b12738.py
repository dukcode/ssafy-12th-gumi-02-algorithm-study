def lower_bound(arr, target):
    st = 0
    en = len(arr)

    while st < en:
        half = (st + en) // 2
        if arr[half] < target:
            st = half + 1
            continue

        en = half

    return st


n = int(input())
arr = list(map(int, input().split()))

cache = []
for idx in range(n):
    num = arr[idx]
    l = lower_bound(cache, num)
    if l == len(cache):
        cache.append(num)
    else:
        cache[l] = num

print(len(cache))
