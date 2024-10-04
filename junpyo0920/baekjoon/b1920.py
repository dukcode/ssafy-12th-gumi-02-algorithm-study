def bin_search(target, s, e):
    mid = (s + e) // 2

    if arr[mid] == target:
        return 1
    if s >= e:
        return 0

    if arr[mid] < target:
        return bin_search(target, mid + 1, e)
    else:
        return bin_search(target, s, mid - 1)


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()

for target in targets:
    print(bin_search(target, 0, n - 1))
