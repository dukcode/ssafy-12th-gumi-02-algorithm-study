

def solve(p, pa, pb):

    try_a = 0
    l = 1
    r = p
    while l <= r:
        try_a += 1
        c = int((l+r) / 2)
        if c == pa:
            break
        elif pa > c:
            l = c
        else:
            r = c

    try_b = 0
    l = 1
    r = p
    while l <= r:
        try_b += 1
        c = int((l + r) / 2)
        if c == pb:
            break
        elif pb > c:
            l = c
        else:
            r = c


    if try_a < try_b:
        return 'A'
    elif try_a > try_b:
        return 'B'
    else:
        return 0

t = int(input())
for tc in range(1, t + 1):
    p, pa, pb = map(int, input().split())
    print(f'#{tc} {solve(p, pa, pb)}')