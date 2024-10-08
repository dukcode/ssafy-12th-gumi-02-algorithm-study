N = int(input())
num = list(map(int, input().split()))


def find(start, end):
    while start <= end:
        mid = (start + end) // 2

        if num[mid] == mid:
            return mid

        elif num[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

    return -1


print(find(0, N - 1))
