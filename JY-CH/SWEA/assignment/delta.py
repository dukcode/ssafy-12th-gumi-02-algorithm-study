arr = [
    [1, 2, 3, 4, 5],
    [9, 8, 7, 6, 5],
    [10, 11, 12, 13, 14],
    [20, 19, 18, 17, 16],
    [9, 8, 7, 6, 5]
]
#     상  하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# #    우상 우하 좌하 좌상
# dr = [-1, 1, 1, -1]
# dc = [1, 1, -1, -1]

r, c = 2, 2  # 현재 위치
for d in range(4):
    print(arr[r + dr[d]][c + dc[d]])
# print(arr[r + dr[0]][c + dc[0]])
# print(arr[r + dr[1]][c + dc[1]])
# print(arr[r + dr[2]][c + dc[2]])
# print(arr[r + dr[3]][c + dc[3]])
print('-----------------------------')
# 현재 위치를 기준으로 길이 K 만큼 검사하기
K = 2
for i in range(1, K + 1):
    # 상하 좌우로 순회
    for d in range(4):
        nr = r + dr[d] * i
        nc = c + dc[d] * i
        print(arr[nr][nc])
print('--------------------')
for d in range(4):
    # 각 방향마다 K번 검사
    for k in range(1, K + 1):
        nr = r + dr[d] * k
        nc = c + dc[d] * k
        print(arr[nr][nc])
print('--------------------------')
# 배열에서 오른쪽 아래쪽 왼쪽 위쪽 으로 각각 세칸씩 움직이면서 출력하기
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c = 0, 0
for d in range(4):  # 네 방향 순서대로 이동
    # 각 방향에서 세 번씩 움직이기
    for i in range(3):
        # r += dr[d]
        # c += dc[d]
        r = r + dr[d]
        c = c + dc[d]
        print(arr[r][c])



