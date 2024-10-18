# 3
# 15
# 27
# 12


def quick_sort(start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(start, right - 1)
    quick_sort(right + 1, end)


def counting_sort():
    counts = [0] * (max(arr) + 1)

    for num in arr:
        counts[num] += 1

    idx = 0
    for num in range(len(counts)):
        for _ in range(counts[num]):
            arr[idx] = num
            idx += 1


n = int(input())
arr = [int(input()) for _ in range(n)]
# quick_sort(0, n - 1)
counting_sort()
print(arr)
