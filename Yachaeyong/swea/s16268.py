# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     balloon = [list(map(int, input().split())) for _ in range(N)]
# 
# 
#     def solve(arr):
# 
#         dr = [0, 1, 0, -1]
#         dc = [1, 0, -1, 0]
# 
#         sum_total = [[0] * M for _ in range(N)]
#         # 행 방향으로 순회하며 꽃가루 개수 더하기
#         for r in range(N):
#             for c in range(M):
#                 for k in range(4):
#                     nr = r + dr[k]
#                     nc = c + dc[k]
#                     # 인덱스 에러 방지
#                     if 0 <= nr < N and 0 <= nc < M:
#                         # 인접 4방향 꽃가루 개수 다 더하기
#                         sum_total[r][c] += arr[nr][nc]
#                 # 기준 위치 꽃가루 수 더하기
#                 sum_total[r][c] += arr[r][c]
#         max_v = 0
#         # 꽃가루 최대 개수 구하기
#         for i in range(N):
#             for j in range(M):
#                 if sum_total[i][j] > max_v:
#                     max_v = sum_total[i][j]
# 
#         return max_v
# 
#     print(f'#{tc} {solve(balloon)}')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloon = [list(map(int, input().split())) for _ in range(N)]


    def solve(arr):
        # 기준/우/하/좌/상
        dr = [0, 0, 1, 0, -1]
        dc = [0, 1, 0, -1, 0]

        sum_total = [[0] * M for _ in range(N)]
        # 행 방향으로 순회하며 꽃가루 개수 더하기
        for r in range(N):
            for c in range(M):
                for k in range(5):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    # 인덱스 에러 방지
                    if 0 <= nr < N and 0 <= nc < M:
                        # 인접 기준위치 + 인접 4방향 꽃가루 개수 다 더하기
                        sum_total[r][c] += arr[nr][nc]
        max_v = 0
        # 꽃가루 최대 개수 구하기
        for i in range(N):
            for j in range(M):
                if sum_total[i][j] > max_v:
                    max_v = sum_total[i][j]

        return max_v

    print(f'#{tc} {solve(balloon)}')
