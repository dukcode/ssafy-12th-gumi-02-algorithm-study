# 줄기세포 배양

# 하나의 줄기세포 크기 : 1 x 1
# x 시간동안 비활성화 상태 x 시간 지나는 순간 활성 상태
# 활성 상태인 경우 x 시간 살아있을 수 있으며 x시간이 지나면 죽게 된다.
# 죽더라도 죽은 상태로 셀을 차지함
# 활성화 되면 첫 1시간 동안 상하좌우로 번식
# 번식된 세포는 비활성 상태
# 해당 셀에 이미 세포 존재하는 경우 추가 번식 못함
# 2개 이상의 세포가 동시에 한 셀로 번식하려는 경우 생명력 수치가 높은 세포가 번식하게 됨

# k 시간 후 살아있는 세포 갯수 구하기

MX = 1000
BLANK = -2
DEAD = -1
INACTIVE = 0
NEW = 0
ACTIVE = 2

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)

t = int(input())  #
for tc in range(1, t + 1):
    h, w, k = map(int, input().split())  # h, w : 1 ~ 50, k : 1 ~ 300
    initial = [list(map(int, input().split())) for _ in range(h)]

    # (생명력, 남은 시간, 상태)
    board = [[(0, 0, BLANK)] * MX for _ in range(MX)]

    for y in range(h):
        for x in range(w):
            board[y + 500][x + 500] = (initial[y][x], initial[y][x], INACTIVE)

    for _ in range(k):
        # 하나의 줄기세포 크기 : 1 x 1
        # x 시간동안 비활성화 상태 x 시간 지나는 순간 활성 상태
        # 활성 상태인 경우 x 시간 살아있을 수 있으며 x시간이 지나면 죽게 된다.
        # 죽더라도 죽은 상태로 셀을 차지함
        # 활성화 되면 첫 1시간 동안 상하좌우로 번식
        # 번식된 세포는 비활성 상태
        # 해당 셀에 이미 세포 존재하는 경우 추가 번식 못함
        # 2개 이상의 세포가 동시에 한 셀로 번식하려는 경우 생명력 수치가 높은 세포가 번식하게 됨

        for y in range(MX):
            for x in range(MX):
                # (생명력, 남은 시간, 상태)
                cell = board[y][x]

                if cell[2] == INACTIVE:
                    time = cell[1] - 1
                    if time == 0:
                        board[y][x] = (cell[0], cell[0], ACTIVE)
                    else:
                        board[y][x] = (cell[0], time, INACTIVE)

                    continue

                if cell[2] == ACTIVE:
                    energy = cell[0]
                    time = cell[1] - 1
                    if time == 0:
                        for dir in range(4):
                            ny = y + dy[dir]
                            nx = x + dx[dir]
                            if board[ny][nx][2] == BLANK or board[ny][nx][2] == NEW:
                                if board[ny][nx][0] < energy:
                                    board[ny][nx] = (energy, energy, NEW)
                        board[y][x] = (cell[0], 0, DEAD)
                    else:
                        board[y][x] = (cell[0], time, ACTIVE)

                    continue
