for tc in range(int(input())):
    n, m = map(int, input().split())
    ans = "ON"
    for i in range(n):
        if not m & (1 << i):
            ans = "OFF"
    print(f"#{tc+1} {ans}")