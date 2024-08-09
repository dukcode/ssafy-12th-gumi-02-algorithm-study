# 색종이

white_board = [[0] * 100 for _ in range(100)]

N = int(input())


for _ in range(N):
    R, C = map(int, input().split())
    # 색종이 길이 10이니 더하기
    for r in range(R, R+10):
        for c in range(C, C+10):
            white_board[r][c] = 1
            
count = 0
for i in range(100):
        for j in range(100):
             if white_board[i][j] == 1:
                  count += 1

print(count)
