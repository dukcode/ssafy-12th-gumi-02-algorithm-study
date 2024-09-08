def solve(idx=0, cnt=0):
    global ans

    if idx >= n - 1:
        ans = min(ans, cnt - 1)
        return

    if cnt >= ans:
        return

    for i in range(1, data[idx] + 1):
        solve(idx + i, cnt+1)


for tc in range(int(input())):
    n, *data = map(int, input().split())
    ans = 0xFFFFFFFF
    solve(0)
    print(f"#{tc+1} {ans}")
