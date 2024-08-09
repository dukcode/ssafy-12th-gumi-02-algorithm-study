t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [input() for _ in range(n)]

    half = n // 2

    ans = 0
    for y in range(n):
        for x in range(abs(half - y), n - abs(y - half)):
            ans += int(arr[y][x])

    print(f"#{tc} {ans}")
