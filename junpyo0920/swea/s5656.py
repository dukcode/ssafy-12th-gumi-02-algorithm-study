from copy import deepcopy


def get_score():
    ret = 0
    for y in range(h):
        for x in range(w):
            if sample_data[y][x]:
                ret += 1
    return ret


def init_sample_data():
    global sample_data
    sample_data = deepcopy(data)
    return


def init_visited():
    global visited
    visited = [[0] * w for _ in range(h)]
    return


def drop_all_blocks():
    for x in range(w):
        blocks = []
        for y in range(h):
            if sample_data[y][x]:
                blocks.append(sample_data[y][x])

        for y in range(h - 1, -1, -1):
            if sample_data[y][x]:
                sample_data[y][x] = 0
            if blocks:
                sample_data[y][x] = blocks.pop()
    init_visited()
    return
    

def explode(y, x):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited[y][x] = 1

    for d in range(4):
        for r in range(1, sample_data[y][x]):
            ny = y + (dy[d] * r)
            nx = x + (dx[d] * r)

            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and sample_data[ny][nx]:
                explode(ny, nx)

    sample_data[y][x] = 0
    return


def get_y_axis(x):
    for y in range(h):
        if sample_data[y][x]:
            return y
    return -1


def finish_game():
    global ans
    score = get_score()
    ans = min(ans, score)
    init_sample_data()


def solve2(arr, idx=0):
    if idx == n:
        for x in arr:
            y = get_y_axis(x)
            if y == -1:
                finish_game()
                return
            explode(y, x)
            drop_all_blocks()

        finish_game()
        return

    for i in range(w):
        arr[idx] = i
        solve2(arr, idx + 1)
        arr[idx] = 0


for tc in range(int(input())):
    n, w, h = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    sample_data = deepcopy(data)

    ans = 0xFFFFFFFF
    solve2([0] * n)
    print(f"#{tc+1} {ans}")