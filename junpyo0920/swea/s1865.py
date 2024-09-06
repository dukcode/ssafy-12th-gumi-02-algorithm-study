def solve(idx=0, total_sum=1.0):
    global ans
    if total_sum < ans:
        return

    if idx == n:
        ans = max(ans, total_sum)
        return

    state = (idx, tuple(done))
    if state in memo and total_sum <= memo[state]:
        return
    else:
        memo[state] = total_sum

    for i in range(n):
        if not done[i]:
            done[i] = 1
            solve(idx + 1, total_sum * data[idx][i])
            done[i] = 0


for tc in range(int(input())):
    n = int(input())
    data = [list(map(lambda x: float(x) / 100, input().split())) for _ in range(n)]
    done = [0] * n
    memo = {}
    ans = 0
    solve()
    print(f"#{tc+1} {ans * 100:.6f}")
