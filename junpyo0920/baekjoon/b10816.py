def find_first_index(target, start_index, end_index):
    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if arr[mid] < target:
            start_index = mid + 1
        else:
            end_index = mid - 1
    return start_index


def find_last_index(target, start_index, end_index):
    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if arr[mid] <= target:
            start_index = mid + 1
        else:
            end_index = mid - 1
    return end_index

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()

for target in targets:
    s = 0
    e = n - 1
    first = find_first_index(target, s, e)
    last = find_last_index(target, s, e)
    print(last - first + 1, end=" ")
