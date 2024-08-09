# 탱크가 반드시 포함된 H x W 크기의 맵이 주어지고
# 탱크의 행동(이동, 공격)이 주어질 때,
# 모든 행동을 수행한 이후 맵을 출력하는 문제

def tank_shoot():
    cur_y = cur_pos[0][0]
    cur_x = cur_pos[0][1]
    walls = ['#', '*']

    if cur_pos[1] == '<':
        bul_move = [0, cur_x]
        while bul_move[1] - 1 >= 0:
            bul_move[1] -= 1
            if field[cur_y][bul_move[1]] in walls:
                if field[cur_y][bul_move[1]] == '*':
                    field[cur_y][bul_move[1]] = '.'
                break
    elif cur_pos[1] == '>':
        bul_move = [0, cur_x]
        while bul_move[1] + 1 < len(field[0]):
            bul_move[1] += 1
            if field[cur_y][bul_move[1]] in walls:
                if field[cur_y][bul_move[1]] == '*':
                    field[cur_y][bul_move[1]] = '.'
                break
    elif cur_pos[1] == 'v':
        bul_move = [cur_y, 0]
        while bul_move[0] + 1 < len(field):
            bul_move[0] += 1
            if field[bul_move[0]][cur_x] in walls:
                if field[bul_move[0]][cur_x] == '*':
                    field[bul_move[0]][cur_x] = '.'
                break
    elif cur_pos[1] == '^':
        bul_move = [cur_y, 0]
        while bul_move[0] - 1 >= 0:
            bul_move[0] -= 1
            if field[bul_move[0]][cur_x] in walls:
                if field[bul_move[0]][cur_x] == '*':
                    field[bul_move[0]][cur_x] = '.'
                break


def tank_move(move):
    cur_y = cur_pos[0][0]
    cur_x = cur_pos[0][1]

    if move == 'U':
        if cur_y - 1 >= 0 and field[cur_y - 1][cur_x] == '.':
            field[cur_y][cur_x] = '.'
            cur_y -= 1
            cur_pos[0][0] = cur_y
        cur_pos[1] = '^'
        field[cur_y][cur_x] = cur_pos[1]
    elif move == 'L':
        if cur_x - 1 >= 0 and field[cur_y][cur_x - 1] == '.':
            field[cur_y][cur_x] = '.'
            cur_x -= 1
            cur_pos[0][1] = cur_x
        cur_pos[1] = '<'
        field[cur_y][cur_x] = cur_pos[1]
    elif move == 'D':
        if cur_y + 1 < len(field) and field[cur_y + 1][cur_x] == '.':
            field[cur_y][cur_x] = '.'
            cur_y += 1
            cur_pos[0][0] = cur_y
        cur_pos[1] = 'v'
        field[cur_y][cur_x] = cur_pos[1]
    elif move == 'R':
        if cur_x + 1 < len(field[0]) and field[cur_y][cur_x + 1] == '.':
            field[cur_y][cur_x] = '.'
            cur_x += 1
            cur_pos[0][1] = cur_x
        cur_pos[1] = '>'
        field[cur_y][cur_x] = cur_pos[1]


for tc in range(int(input())):
    H, W = map(int, input().split())
    field = []
    cur_pos = [[int(), int()], '']
    
    for y in range(H):
        line = list(map(str, input()))
        field.append(line)
        for obj in line:
            if obj in ['<', '>', '^', 'v']:
                cur_pos = [[y, line.index(obj)], obj]
    
    N = int(input())
    actions = list(map(str, input()))

    for action in actions:
        if action == 'S':
            tank_shoot()
        else:
            tank_move(action)
    
    for idx, line in enumerate(field) :
        if idx == 0: print(f'#{tc + 1}', end=' ')
        print(''.join(line))
