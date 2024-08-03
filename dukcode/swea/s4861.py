dirs = ((0, 1), (1, 0))

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    words = list()
    for _ in range(n):
        words.append(input())

    def in_range(y, x):
        return 0 <= y < n and 0 <= x < n

    def is_palindrome(sy, sx, dir):
        ey = sy + (m - 1) * dirs[dir][0]
        ex = sx + (m - 1) * dirs[dir][1]

        while abs(ey - sy) > 1 or abs(ex - sx) > 1:
            if not in_range(sy, sx) or not in_range(ey, ex):
                return False

            if words[sy][sx] != words[ey][ex]:
                return False

            sy += dirs[dir][0]
            sx += dirs[dir][1]
            ey -= dirs[dir][0]
            ex -= dirs[dir][1]

        return True

    def find_palindrome():
        for y in range(n):
            for x in range(n):
                for dir in range(2):
                    if is_palindrome(y, x, dir):
                        return (y, x, dir)

    y, x, dir = find_palindrome()

    print(f"#{tc} ", end="")
    for _ in range(m):
        print(words[y][x], end="")
        y += dirs[dir][0]
        x += dirs[dir][1]
    print()
