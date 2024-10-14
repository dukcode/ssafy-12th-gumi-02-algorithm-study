#subtree


def solve(n):
    global cnt
    if n != 0:
        cnt += 1
        solve(left[n])
        solve(right[n])


T = int(input())
for tc in range(1, T + 1):
    e, n = map(int, input().split())
    left = [0] * (e + 2)
    right = [0] * (e + 2)
    edges = list(map(int, input().split()))
    for i in range(0, e * 2, 2):
        if left[edges[i]] == 0:
            left[edges[i]] = edges[i + 1]
        else:
            right[edges[i]] = edges[i + 1]

    cnt = 0
    solve(n)
    print(f'#{tc} {cnt}')