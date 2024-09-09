def solve(idx, remain, cnt):
    global change
    if idx == N - 1:
        change = min(change, cnt)
        return
    if cnt >= change:
        return

    remain -= 1
    solve(idx + 1, battery[idx], cnt + 1)
    if remain > 0:
        solve(idx + 1, remain, cnt)

T = int(input())
for tc in range(1, T + 1):
    N, *battery = map(int, input().split())
    change = 0xffff
    solve(1, battery[0], 0)
    print(f'#{tc} {change}')
