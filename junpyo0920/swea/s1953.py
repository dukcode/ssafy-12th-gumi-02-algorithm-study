from collections import deque

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def get_directions(pipe_num):
    if pipe_num == 1:
        return 0, 1, 2, 3
    elif pipe_num == 2:
        return 0, 2
    elif pipe_num == 3:
        return 1, 3
    elif pipe_num == 4:
        return 0, 1
    elif pipe_num == 5:
        return 1, 2
    elif pipe_num == 6:
        return 2, 3
    else:
        return 3, 0


def is_next_pipe_valid(direction, next_pipe):
    if next_pipe == 1:
        return True

    if direction == 0 and next_pipe in [2, 5, 6]:
        return True
    if direction == 1 and next_pipe in [3, 6, 7]:
        return True
    if direction == 2 and next_pipe in [2, 4, 7]:
        return True
    if direction == 3 and next_pipe in [3, 4, 5]:
        return True

    return False

def get_count(moves):
    ret = 0
    for y in range(h):
        for x in range(w):
            if moves[y][x]:
                ret += 1
    return ret


def move_all_roots(start_pos):
    q = deque((start_pos, ))
    visited = [[0] * w for _ in range(h)]
    visited[start_pos[0]][start_pos[1]] = 1

    while q:
        cy, cx = q.popleft()
        directions = get_directions(data[cy][cx])
        for direction in directions:
            ny, nx = cy + dy[direction], cx + dx[direction]
            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and is_next_pipe_valid(direction, data[ny][nx]):
                next_t = visited[cy][cx] + 1
                if next_t <= t:
                    visited[ny][nx] = next_t
                    q.append((ny, nx))

    return visited


for tc in range(int(input())):
    h, w, hole_y, hole_x, t = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(h)]
    moves = move_all_roots((hole_y, hole_x))
    count = get_count(moves)
    print(f'#{tc+1} {count}')