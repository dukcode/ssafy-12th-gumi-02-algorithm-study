dy = [-1, 0, 1, 0, -1, -1, 1, 1]
dx = [0, 1, 0, -1, -1, 1, 1, -1]


def get_flies(y, x, w):
    ret = data[y][x]
    for p in range(1, m):
        if w == 0:
            for d in range(4):
                ny, nx = y + (dy[d] * p), x + (dx[d] * p)
                if 0 <= ny < n and 0 <= nx < n:
                    ret += data[ny][nx]
        elif w == 1:
            for d in range(4, 8):
                ny, nx = y + (dy[d] * p), x + (dx[d] * p)
                if 0 <= ny < n and 0 <= nx < n:
                    ret += data[ny][nx]
        else:
            return -1
    return ret


for tc in range(int(input())):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    ans = -0xFFFFFFFF
    for y in range(n):
        for x in range(n):
            for way in range(2):
                ans = max(ans, get_flies(y, x, way))

    print(f"#{tc+1} {ans}")
