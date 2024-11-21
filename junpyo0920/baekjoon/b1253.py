n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

for i in range(n):
    st = 0
    en = n - 1

    while st < en:
        if i == st:
            st += 1
            continue

        if i == en:
            en -= 1
            continue

        if arr[st] + arr[en] < arr[i]:
            st += 1
        elif arr[st] + arr[en] > arr[i]:
            en -= 1
        else:
            ans += 1
            break

print(ans)