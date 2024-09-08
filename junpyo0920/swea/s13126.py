def solve(dep=0, total_price=0):
    global ans
    if total_price > ans:
        return

    if dep == n:
        ans = min(ans, total_price)

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            solve(dep + 1, total_price + data[dep][i])
            visited[i] = 0


for tc in range(int(input())):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 0xFFFFFFFF
    solve()
    print(f"#{tc+1} {ans}")