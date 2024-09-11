N = int(input())
data = input().split()
r, c = 1, 1
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']

for d in data:
    for i in range(len(dir)):
        if d == dir[i]:
            nr, nc = r + dr[i], c + dc[i]

    if 1 <= nr <= N and 1 <= nc <= N:
        r = nr
        c = nc

print(r, c)
