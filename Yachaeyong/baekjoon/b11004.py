# K번째 수
import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))


# A.sort()
# print(A[K - 1])

# # 퀵 정렬 - 시간 초과
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
# quick_sort(A, 0, N - 1)
# print(A[K - 1])
