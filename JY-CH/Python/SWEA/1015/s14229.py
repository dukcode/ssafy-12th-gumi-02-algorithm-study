# 백만 개의 정수 정렬
def partition(start, end):
    pivot = A[start]
    left = start + 1
    right = end
 
    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while left <= right and A[right] >= pivot:
            right -= 1
 
        if left <= right:
            A[left], A[right] = A[right], A[left]
 
    A[start], A[right] = A[right], A[start]
    return right
 
 
def quick(start, end):
    if start < end:
        p = partition(start, end)
        quick(start, p-1)
        quick(p+1, end)

A = list(map(int, input().split()))
quick(A, 0, len(A) - 1)
print(A[500000])
