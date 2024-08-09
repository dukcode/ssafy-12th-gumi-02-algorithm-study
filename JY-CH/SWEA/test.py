def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return true
        elif a[middle] > key:
            end = middle - 1
        else :
            start = middle + 1
    return false

def bubble_sort(arr):
    cnt = len(arr)
    for i in range(cnt-1, 0, -1):
        for j in range(0, i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([8, 4,7,5,0]))