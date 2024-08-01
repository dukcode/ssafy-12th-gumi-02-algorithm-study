def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    selection_sort(arr)

    ans = []
    for idx in range(10):
        if idx % 2 == 1:
            ans.append(arr[idx // 2])
            continue

        ans.append(arr[n - 1 - idx // 2])

    print(f"#{tc} ", end="")
    print(*ans)
