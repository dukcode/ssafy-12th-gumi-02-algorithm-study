# N-QUEEN

# 2차원 배열 돌며 queen 놓기
def put_queen(y, used_col, used_diag1, used_diag2):
    # 맨 아래 층까지 다 채웠으면,
    if y == N:
        # 키운트 + 1
        global cnt
        cnt += 1
        return

    # 한 층(row)의 column 순회
    for x in range(N):
        # 퀸을 해당 위치의 column에 놓은 적 없고, 우상향 대각에 놓은 적 없고, 우하향 대각에 놓은 적 없으면,
        if not used_col[x] and not used_diag1[y + x] and not used_diag2[(x - y) + (N - 1)]:
            # column 방문 이력 추가
            used_col[x] = 1
            # 우상향 대각 방문 이력 추가
            used_diag1[y + x] = 1
            # 우하향 대각 방문 이력 추가
            used_diag2[(x - y) + (N - 1)] = 1
            # 해당 위치에 퀸 놓음
            put_queen(y+1, used_col, used_diag1, used_diag2)
            # column 방문 이력 삭제
            used_col[x] = 0
            # 우상향 대각 방문 이력 삭제
            used_diag1[y + x] = 0
            # 우하향 대각 방문 이력 삭제
            used_diag2[(x - y) + (N - 1)] = 0


cnt = 0
N = int(input())
put_queen(0, [0] * N, [0] * (N * 2 - 1), [0] * (N * 2 - 1))

print(cnt)
