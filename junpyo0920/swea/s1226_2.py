from collections import deque

w = h = 16
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def get_start():
    ret = (-1, -1)
    for y in range(h):
        for x in range(w):
            if data[y][x] == 2:
                ret = (y, x)
                return ret
    return ret


def can_find_root(start):
    q = deque([start])
    visited = [[0] * w for _ in range(h)]
    visited[q[0][0]][q[0][1]] = 1

    while q:
        cur_y, cur_x = q.popleft()

        for d in range(4):
            next_y, next_x = cur_y + dy[d], cur_x + dx[d]

            if 0 <= next_y < h and 0 <= next_x < w and data[next_y][next_x] == 3:
                return 1

            if 0 <= next_y < h and 0 <= next_x < w and data[next_y][next_x] == 0 and not visited[next_y][next_x]:
                visited[next_y][next_x] = 1
                q.append((next_y, next_x))

    return 0


for _ in range(10):
    tc = int(input())
    data = [list(map(int, list(input()))) for _ in range(h)]
    start = get_start()
    ans = can_find_root(start)
    print(f'#{tc} {ans}')