def solve(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return solve(arr, target, start, mid - 1)
    else:
        return solve(arr, target, mid + 1, end)
    
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr.sort()
for i in range(M):
    result = solve(arr, arr2[i], 0 , N - 1)
    print(result)