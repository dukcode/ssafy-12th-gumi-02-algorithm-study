def make_perm(arr, last_num, idx=0):
    if idx == M:
        print(*arr)
        return
    for num in data:
        if num >= last_num:
            arr[idx] = num
            make_perm(arr, num, idx+1)
            arr[idx] = 0


N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
make_perm([0] * M, 0)