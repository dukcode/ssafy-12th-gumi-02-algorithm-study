# 숫자 카드 2
# 1번이 약 2.5배 빠름

# 1. bisect
from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
target = list(map(int, input().split()))

def count_card(data, left_value, right_value):
    left_idx = bisect_left(data, left_value)
    right_idx = bisect_right(data, right_value)

    return right_idx-left_idx

for t in target:
    print(count_card(cards, t, t), end=' ')

# # 2. 이진 탐색
# def first(data, target, start, end):
#     if start > end:
#         return None
#
#     mid = (start + end) // 2
#
#     if (mid == 0 or data[mid - 1] < target) and data[mid] == target:
#         return mid
#     elif data[mid] >= target:
#         return first(data, target, start, mid - 1)
#     else:
#         return first(data, target, mid + 1, end)
#
#
# def last(data, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#
#     if (mid == N - 1 or data[mid + 1] > target) and data[mid] == target:
#         return mid
#     elif data[mid] > target:
#         return last(data, target, start, mid - 1)
#     else:
#         return last(data, target, mid + 1, end)
#
#
# def count_card(data, target):
#     first_idx = first(data, target, 0, N - 1)
#
#     if first_idx == None:
#         return 0
#
#     last_idx = last(data, target, 0, N - 1)
#
#     return last_idx - first_idx + 1
#
#
# N = int(input())
# cards = list(map(int, input().split()))
# cards.sort()
# M = int(input())
# target = list(map(int, input().split()))
#
# for t in target:
#     print(count_card(cards, t), end=' ')
