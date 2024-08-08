# https://www.acmicpc.net/problem/1926

# 예상 입력값
# 3 3
# 1 1 0
# 0 1 1
# 1 1 0
# 예상 출력값
# 1
# 6

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    temp_size = 1  # 시작점도 그림 크기에 포함 되어야 함
    stack = [(y, x)]  # 시작점에서 시작
    visited[y][x] = 1  # 시작점을 visited에 추가
    while stack:
        cy, cx = stack[-1]  # 현재 위치
        for d in range(4):  # 상, 하, 좌, 우 탐색
            ny = cy + dy[d]
            nx = cx + dx[d]
            # 탐색한 경로가 유효 범위 내에 있고 이동 가능한 경로이며 방문 이력이 없으면,
            if 0 <= ny < h and 0 <= nx < w and data[ny][nx] and not visited[ny][nx]:
                stack.append((ny, nx))
                visited[ny][nx] = 1
                temp_size += 1
                break
        else:
            stack.pop()
    return temp_size


h, w = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]
visited = [[0] * w for _ in range(h)]

cnt_pic = 0
size = 0
# 주어진 그림 전체 탐색
for y in range(h):
    for x in range(w):
        # 방문한 이력이 없는 그림 시작점을 찾으면,
        if data[y][x] and not visited[y][x]:
            # 그림 개수 추가
            cnt_pic += 1
            # 그림 크기 탐색
            result = dfs(y, x)
            size = result if size < result else size

print(cnt_pic)
print(size)
