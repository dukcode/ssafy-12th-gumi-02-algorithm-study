# 퀵 정렬
def quick(arr, start, end):
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
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
 
    quick(arr, start, right - 1)
    quick(arr, right + 1, end)


for tc in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    quick(a, 0, n - 1)
    print(f'#{tc+1} {a[n//2]}')