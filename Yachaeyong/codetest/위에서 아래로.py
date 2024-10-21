import sys

input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]


print(arr)
#1. 내장함수
arr.sort(reverse=True)
print(*arr)

# 2. 선택정렬
for i in range(N):
    max_idx = i
    for j in range(i + 1, N):
        if arr[max_idx] < arr[j]:
            max_idx = j
    arr[i], arr[max_idx] = arr[max_idx], arr[i]

print(arr)

# # 3. 퀵 정렬
# def quick_sort(arr, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start + 1
#     right = end
#
#     while left <= right:
#         while left <= end and arr[left] <= arr[pivot]:
#             left += 1
#         while right > start and arr[right] >= arr[pivot]:
#             right -= 1
#
#         if left > right:
#             arr[right], arr[pivot] = arr[pivot], arr[right]
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#
#     quick_sort(arr, start, right - 1)
#     quick_sort(arr, right + 1, end)
#
#
# quick_sort(arr, 0, N - 1)
# print(*reversed(arr))

# # 4. 카운트 정렬(계수 정렬)
# counts = [0] * (max(arr)+1)
# M = len(counts)
# temp = [0] * N
#
# for i in range(N):
#     counts[arr[i]] += 1
#
# for i in range(1, M):
#     counts[i] += counts[i-1]
#
# for i in range(N-1, -1, -1):
#     counts[arr[i]] -= 1
#     temp[counts[arr[i]]] = arr[i]
#
# print(*reversed(temp))
