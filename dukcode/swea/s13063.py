MX = 987_654_321


def solve(y, x):
    if y < 0 or x < 0:
        return MX

    if y == 0 and x == 0:
        return board[0][0]

    if cache[y][x] != -1:
        return cache[y][x]

    ret = board[y][x] + min(solve(y - 1, x), solve(y, x - 1))
    cache[y][x] = ret
    return ret


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    cache = [[-1] * n for _ in range(n)]

    print(f"#{tc} {solve(n - 1, n - 1)}")
