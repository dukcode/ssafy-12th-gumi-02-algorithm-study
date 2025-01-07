# 떡볶이 떡 만들기

def binary_search(arr, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for cut in arr:
            if cut > mid:
                total += cut - mid

        if total < m:
            end = mid - 1

        else:
            result = mid
            start = mid + 1
    return(result)
        
n, m = map(int, input().split())
cake = list(map(int, input().split()))
start = 0
end = max(cake)
answer = binary_search(cake, start, end)
print(answer)

