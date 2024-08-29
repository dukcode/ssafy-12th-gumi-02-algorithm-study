def solve1(l, page, r):
    mid = (r + l)//2
    if mid == page:
        return 1
    elif mid > page:
        return solve1(l, page, mid) + 1
    elif mid < page:
        return solve1(mid, page, r) + 1


T = int(input())
for tc in range(1, T + 1):
    P, a, b = map(int, input().split())
    A = 0
    B = 0
    if a > P / 2:
        A += solve1(P/2, a, P)
    elif a < P / 2:
        A += solve1(1, a, P/2)

    if b > P / 2:
        B += solve1(P/2, b, P)
    elif b < P / 2:
        B += solve1(1, b, P/2)

    if A > B:
        print(f'#{tc} B')
    elif A < B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')