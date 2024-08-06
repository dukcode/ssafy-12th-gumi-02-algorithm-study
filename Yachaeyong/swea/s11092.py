# 최대 최소의 간격

for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0
    max_idx = 0
    min_v = 11
    min_idx = 0

    for i in range(N):
        if  max_v <= arr[i]:
            max_v = arr[i]
            max_idx = i
    for idx in range(N-1, -1, -1):
        if arr[idx] == max_v:
            max_idx = idx
            break

    for j in range(N):
        if min_v >= arr[j]:
            min_v = arr[j]
            min_idx = j
            
    for idx in range(N):
        if arr[idx] == min_v:
            min_idx = idx
            break

    if max_idx - min_idx < 0:
        result = -(max_idx - min_idx)
    else: result = max_idx - min_idx

    print(f'#{tc+1} {result}')