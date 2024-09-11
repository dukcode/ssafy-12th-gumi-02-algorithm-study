N, M = map(int, input().split())
r, c, dir = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
# 북동남서 = 상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

cnt = 1
turn_cnt = 0
while True:
    turn_left()
    nr = r + dr[dir]
    nc = c + dc[dir]
    # 육지고 아직 안 갔으면 이동
    if not game_map[nr][nc] and not visited[nr][nc]:
        visited[nr][nc] = 1
        r = nr
        c = nc
        cnt += 1
        turn_cnt = 0
        continue

    # 바다면 회전만 하고 돌아감
    else:
        turn_cnt += 1

    # 인접 4칸이 모두 가봤거나 바다인 경우
    if turn_cnt == 4:
        # 방향 유지하고 뒤로 1칸 이동
        nr = r - dr[dir]
        nc = c - dc[dir]
        if not game_map[nr][nc]:
            r = nr
            c = nc
        # 바다면 종료
        else:
            break

        turn_cnt = 0

print(cnt)
