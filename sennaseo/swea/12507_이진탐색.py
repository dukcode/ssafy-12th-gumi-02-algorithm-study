def solve1(l, page, p):
    k = p + l
    if p == page:
        return 1
    elif k/2 > page:
        return solve1(l, page, k / 2 ) + 1
    else:
        return solve1(k / 2, page, p) + 1


T = int(input())
for tc in range(1, T+1):
    P, a, b = map(int, input().split())
    if a > P/2:
        A = solve1(P/2, a, ((P/2)+P)/2)
    elif a < P/2:
        A = solve1(0, a, P/2)

    if b > P/2:
        B = solve1(P/2, b, ((P/2)+P)/2)
    elif b < P/2:
        B = solve1(0, a, P/2)
    
    if A > B:
        result = 'B'
    elif A < B:
        result = 'A'
    elif A == B:
        result = 0
    
    print(f'#{tc} {result}')