# 위에서 아래로

# sort 사용
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

# sort 사용
# arr = sorted(arr)

# for idx in range(n):
#     print(arr[n-idx-1], end=' ')

# 선택 정렬
for idx in range(n):
    min_idx = idx
    for compare_idx in range(idx + 1, n):
        if arr[min_idx] > arr[compare_idx]:
            min_idx = compare_idx
    
    arr[idx], arr[compare_idx] = arr[compare_idx], arr[idx]

# print(arr)
for idx in range(n):
    print(arr[n-idx-1], end=' ')

# 삽입 정렬
for idx in range(1, len(arr)):
    # 첫번째는 정렬이 되있다고 판단
    for compare_idx in range(idx, 0, -1):
        if arr[compare_idx] < arr[compare_idx-1]:
            arr[compare_idx], arr[compare_idx-1] = arr[compare_idx-1], arr[compare_idx]
        else:
            break

# print(arr)
for idx in range(n):
    print(arr[n-idx-1], end=' ')

# 퀵 정렬

def quick(arr, start, end):
    # 원소가 1개면 종료
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    # 좌 우 1개씩 탐색하면서
    # 기준되는 pivot 보다 왼쪽값이 큰지, 오른쪽값이 작은지 체크
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -=1

        # 탐색 도중 왼쪽이 오른쪽보다 커졌다는건?
        # 값이 엇갈린것.
        # pivot 자체를 바꿔서 다시 시작
        if left > right:
            # 작은 값을 pivot으로
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            # 아니면 좌 우 교환
            arr[left], arr[right] = arr[right], arr[left]

    # 값을 교환했으므로 현재 pivot = right
    # 피벗 기준으로 나눠진 왼쪽 오른쪽 재귓
    quick(arr, start, right-1)
    quick(arr, right + 1, end)

# 첫번째 데이터 피벗 설정해서 하나 빼야됨
quick(arr, 0, len(arr) - 1)

# print(arr)
for idx in range(n):
    print(arr[n-idx-1], end=' ')

# 계수 정렬

# 일단 전부 0보다 크다
# 모든 범위 포함 리스트 생성
# 가장 큰값 + 가장 작은값 0
count = [0] * (max(arr) + 1)

# 카운트 배열에 맞는 숫자는 값을 올림
for idx in range(len(arr)):
    count[arr[idx]] += 1

# 카운트 배열을 돌면서
for i in range(len(count)):
    # 계수만큼 도니까 출력하면 정렬 가능
    for j in range(count[i]):
        print(i, end=' ')
