dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def get_y_axis(arr):
    for y in range(h):
        if arr[y]:
            return y
    return -1


def shoot(cnt, remains, cur_data):
    if not cnt or not remains:
        global ans
        ans = min(ans, remains)
        return

    for x in range(w):
        copied_data = [row[:] for row in cur_data]

        y = -1
        for i in range(h):
            if copied_data[i][x]:
                y = i
                break

        if y == -1:
            continue

        stack = [(y, x, copied_data[y][x])]
        copied_data[y][x] = 0
        cur_remains = remains - 1

        while stack:
            cy, cx, power = stack.pop()
            for p in range(1, power):
                for d in range(4):
                    ny, nx = cy + (dy[d] * p), cx + (dx[d] * p)
                    if 0 <= ny < h and 0 <= nx < w and copied_data[ny][nx]:
                        stack.append((ny, nx, copied_data[ny][nx]))
                        cur_remains -= 1
                        copied_data[ny][nx] = 0

        for c in range(w):
            r_for_change = h - 1
            for r in range(h-1, -1, -1):
                if copied_data[r][c]:
                    copied_data[r][c], copied_data[r_for_change][c] = copied_data[r_for_change][c], copied_data[r][c]
                    r_for_change -= 1

        shoot(cnt - 1, cur_remains, copied_data)


for tc in range(int(input())):
    n, w, h = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(h)]

    block_cnt = 0
    for y in range(h):
        for x in range(w):
            if data[y][x]:
                block_cnt += 1

    ans = 0xFFFFFFFF
    shoot(n, block_cnt, data)
    print(f"#{tc+1} {ans}")