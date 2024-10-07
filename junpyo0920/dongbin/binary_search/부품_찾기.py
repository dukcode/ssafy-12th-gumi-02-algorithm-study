n = int(input())
arr = sorted(list(map(int, input().split())))

m = int(input())
targets = list(map(int, input().split()))

ans = [''] * m

for (i, target) in enumerate(targets):
    s = 0
    e = n

    while s <= n:
        mid = (s + e) // 2

        if arr[mid] == target:
            ans[i] = 'yes'
            break

        if arr[mid] < target:
            s = mid + 1
            break

        if arr[mid] > target:
            e = mid - 1
            break

    if not ans[i]:
        ans[i] = 'no'

print(*ans)
