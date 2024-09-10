pos = input()
r = int(pos[1])
c = int(ord(pos[0]) - ord('a')) + 1

cnt = 0
for dr, dc in [[-1, 2], [1, 2], [-1, -2], [1, -2], [-2, 1], [-2, -1], [2, 1], [2, -1]]:
    nr, nc = r + dr, c + dc
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        cnt += 1
print(cnt)
