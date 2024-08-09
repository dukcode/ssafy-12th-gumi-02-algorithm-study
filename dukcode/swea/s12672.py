TRUE = 1
FALSE = 0

dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))


def find_start():
    for y in range(n):
        for x in range(n):
            if board[y][x] == 2:
                return y, x


def dfs(here):
    """here에서 갈 수 있는지 여부를 리턴하는 함수"""
    visited[here[0]][here[1]] = True

    # base case
    if board[here[0]][here[1]] == 3:
        return TRUE

    for dir in dirs:
        ny = here[0] + dir[0]
        nx = here[1] + dir[1]

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue

        if visited[ny][nx]:
            continue

        if board[ny][nx] == 1:
            continue

        if dfs((ny, nx)) == TRUE:
            return TRUE

    return FALSE


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    start = find_start()

    ans = dfs(start)

    print(f"#{tc} {ans}")
