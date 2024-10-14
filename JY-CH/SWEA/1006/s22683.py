# 나무 베기

from collections import deque

# 상 우 하 좌
DY = (-1, 0, 1, 0)
DX = (0, 1, 0, -1)

def start():
    for i in range(n):
        for j in range(n):
            if field[i][j] == 'X':
                return i, j


def direction_change(now, next):
    # 현재와 다음 진행방향이 동일하면
    if now == next:
        return 0
    # 현재와 다음 진행방향이 90도 차이나면
    if now % 2 != next % 2:
        return 1
    # 현재와 다음 진행방향이 180도 차이나면
    return 2

def find(sy, sx, direction = 0, cost = 0, cut = 0):
    global ans
    # 이동턴을 더 쓰거나 나무를 제한이상으로 자를 경우
    if cost > ans or cut > k:
        return

    # 도착지 도착했고 나무를 최대치보다 같거나 작게 잘랐을때
    if field[sy][sx] == 'Y' and cut <= k:
        # 최소값을 할당
        ans = min(ans, cost)
        return

    for next_direction in range(4):
        ny = sy + DY[next_direction]
        nx = sx + DX[next_direction]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:  # 범위 체크 추가
            visited[ny][nx] = 1
            # 재귀, 백트래킹
            find(ny, nx, next_direction,
                 cost + 1 + direction_change(direction, next_direction),
                 cut + (1 if field[ny][nx] == 'T' else 0))
            # 초기화
            visited[ny][nx] = 0


t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    field = [list(map(str, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    ans = 0xFFFFFFFF
    y, x = start()
    find(y, x)
    print(f'#{tc} {(ans if ans != 0xFFFFFFFF else -1)}')


# 0xFFFFFFFF도 답에 영향을 준다.
# 이 문제 상하좌우 특정 순서로 바꾸면 답이 틀려진다.