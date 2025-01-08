# 부품 찾기

# 이진 탐색 함수 정의
def binary_search(data, answer, start, end):
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == answer:
            return mid

        elif data[mid] > answer:
            end = mid - 1

        else:
            start = mid + 1

    return None

n = int(input())
data = list(map(int, input().split()))
# 안하면 탐색 불가능
data.sort()
m = int(input())
find = list(map(int, input().split()))

for item in find:
    result = binary_search(data, item, 0, n-1)
    print('yes' if result != None else 'no', end=' ')