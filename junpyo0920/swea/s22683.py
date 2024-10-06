dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def find_start():
    ret = -1, -1
    for y in range(n):
        for x in range(n):
            if data[y][x] == 'X':
                return y, x
    return ret


def get_turn_cost(cur_dir, next_dir):
    if cur_dir == next_dir:
        return 0
    if cur_dir % 2 != next_dir % 2:
        return 1
    return 2


def dfs(cy, cx, direction=0, cost=0, tree_cuts=0):
    global ans
    if cost > ans or tree_cuts > t:
        return

    if data[cy][cx] == 'Y' and tree_cuts <= t:
        ans = min(ans, cost)
        return

    for d in range(4):
        ny, nx = cy + dy[d], cx + dx[d]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs(ny, nx, d, cost + 1 + get_turn_cost(direction, d), tree_cuts + (1 if data[ny][nx] == 'T' else 0))
            visited[ny][nx] = 0


for tc in range(int(input())):
    n, t = map(int, input().split())
    data = [list(input()) for _ in range(n)]
    sy, sx = find_start()
    ans = 0xFFFFFFFF
    visited = [[0] * n for _ in range(n)]
    dfs(sy, sx)
    print(f'#{tc + 1} {ans if ans != 0xFFFFFFFF else -1}')

# 1
# 4 1
# TTTT
# XTTY
# TTTT
# TTTT