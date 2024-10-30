def solve(idx, used_col, current_sum):
    global min_v

    if idx == N:
        min_v = min(min_v, current_sum)
        return
    if current_sum >= min_v:
        return

    for j in range(N):
        if j not in used_col:
            used_col.append(j)
            solve(idx + 1, used_col, current_sum + data[idx][j])
            used_col.pop()

    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_v = 21e8
    solve(0, [], 0)
    print(f"#{tc} {min_v}")
