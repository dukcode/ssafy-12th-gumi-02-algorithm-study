import random


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    pivot_idx = random.randrange(0, len(arr))
    pivot = arr[pivot_idx]

    left = []
    right = []
    for idx, num in enumerate(arr):
        if idx == pivot_idx:
            continue
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] + right


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"#{tc}", quick_sort(arr)[n // 2])
