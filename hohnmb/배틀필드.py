car_d = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}
def find_start(matrix):
    for i in range(H):
        for j in range(W):
            if matrix[i][j] in '><^v':
                return i, j, car_d[matrix[i][j]]
def solve(my_str, matrix, r, c, d):
    if my_str == 'U':
        tmp = '^'
    elif my_str == 'D':
        tmp = 'v'
    elif my_str == 'L':
        tmp = '<'
    elif my_str == 'R':
        tmp = '>'
    elif my_str == 'S':
        rs,cs = r, c
        while True:
            rs += d[0]
            cs += d[1]
            if 0<=rs<H and 0<=cs<W:
                if matrix[rs][cs] == '*':
                    matrix[rs][cs] = '.'
                    return matrix, r, c, d
                elif matrix[rs][cs] == '#':
                    return matrix, r, c, d
            else:
                return matrix, r, c, d
 
    d = car_d[tmp]
    if 0<= r+d[0] < H and 0<=c+d[1]<W:
        if matrix[r+d[0]][c+d[1]] == '.':
            matrix[r][c] = '.'
            r = r+ d[0]
            c = c+d[1]
    matrix[r][c] = tmp
    return matrix, r, c, d
 
 
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split()) 
 
    matrix = [list(input()) for _ in range(H)] 
    N = int(input())
    str_1 = input()
 
    r, c, d = find_start(matrix) 
 
    for i in range(N):
        matrix, r, c, d = solve(str_1[i], matrix, r, c, d)
 
    print(f'#{tc}', end=' ')
    for i in range(H):
        print(*matrix[i], sep='')
