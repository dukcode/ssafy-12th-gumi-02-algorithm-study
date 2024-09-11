# 왕실의 나이트

# 8방향 설정
# 상좌 상우 우상 우하 하우 하좌 좌상 좌하

WAY = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2))

pos = input()
y = int(int(pos[1]))
x = int(ord(pos[0])) - int(ord('a')) + 1

cnt = 0
for direction in WAY:
    ny = y + direction[0]
    nx = x + direction[1]

    if ny >= 1 and ny <= 8 and nx >= 1 and nx <= 8:
        cnt += 1
print(cnt)
