def perm(arr, lst_num):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if i >= lst_num:
            arr.append(i)
            lst_num = i
            perm(arr, lst_num)
            arr.pop()
            lst_num = lst_num


N, M = map(int, input().split())
perm([], 0)