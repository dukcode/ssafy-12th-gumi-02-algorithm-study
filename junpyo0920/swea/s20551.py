for tc in range(int(input())):
    a, b, c = map(int, input().split())

    if c < 3 or b < 2:
        print(f"#{tc+1} -1")
        continue

    ans = 0

    if b >= c:
        ans += b - (c - 1)
        b = c - 1

    if a >= b:
        ans += a - (b - 1)
        a = b - 1

    print(f"#{tc+1} {ans}")
