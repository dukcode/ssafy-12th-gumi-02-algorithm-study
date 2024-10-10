def pascal(idx, prev, arr):
    if idx == N:
        return
    for j in range(idx + 1):
        if j == 0:
            arr[idx][j] = 1
        else:
            arr[idx][j] = prev[j - 1] + prev[j]
        print(arr[idx][j], end=" ")
    print()

    pascal(idx + 1, arr[idx], arr)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    print(f"#{tc}")
    pascal(0, [], arr)
