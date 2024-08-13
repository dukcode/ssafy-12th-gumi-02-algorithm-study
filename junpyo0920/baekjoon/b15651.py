def perm(arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        arr.append(i)
        perm(arr)
        arr.pop()


N, M = map(int, input().split())
perm([])
