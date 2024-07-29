t = int(input())
for ts in range(1, t + 1):
    n, q = tuple(map(int, input().split()))

    arr = [0] * n
    for i in range(q):
        l, r = tuple(map(lambda i: int(i) - 1, input().split()))
        for idx in range(l, r + 1):
            arr[idx] = i + 1

    print(f"#{ts} {' '.join(map(str, arr))}")
