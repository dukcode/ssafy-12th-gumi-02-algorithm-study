# 1. 이진탐색
def first_idx(data, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if (mid == 0 or target > data[mid - 1]) and data[mid] == target:
        return mid
    elif data[mid] > target:
        return first_idx(data, target, start, mid - 1)
    else:
        return first_idx(data, target, mid + 1, end)


def last_idx(data, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2

    if (mid == N - 1 or target < data[mid + 1]) and data[mid] == target:
        return mid
    elif data[mid] > target:
        return last_idx(data, target, start, mid - 1)
    else:
        return last_idx(data, target, mid + 1, end)


def count_num(data, X):
    first = first_idx(data, X, 0, N - 1)

    if first == None:
        return 0

    last = last_idx(data, X, 0, N - 1)

    return last - first + 1


N, X = map(int, input().split())
data = list(map(int, input().split()))

ans = count_num(data, X)

if ans == 0:
    print(-1)
else:
    print(ans)

# # 2. bisect 라이브러리 사용
# from bisect import bisect_left, bisect_right
#
# N, X = map(int, input().split())
# data = list(map(int, input().split()))
#
#
# def num_count(data, right_v, left_v):
#     right_idx = bisect_right(data, right_v)
#     left_idx = bisect_left(data, left_v)
#     return right_idx - left_idx
#
#
# ans = num_count(data, X, X)
#
# if ans == 0:
#     print(-1)
# else:
#     print(ans)
