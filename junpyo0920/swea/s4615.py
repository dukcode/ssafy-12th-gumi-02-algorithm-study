def init_game():
    half = (N // 2) - 1
    game_map[half][half] = 2
    game_map[half + 1][half + 1] = 2
    game_map[half][half + 1] = 1
    game_map[half + 1][half] = 1

    for row in game_map:
        print(*row)
    print()

def put_stone(y, x, stone):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    y -= 1
    x -= 1
    game_map[y][x] = stone
    for d in range(8):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < N and game_map[ny][nx] and game_map[ny][nx] != stone:
            stone_2_flip = []
            is_good_2_flip = False
            while 0 <= ny < N and 0 <= nx < N:
                if not game_map[ny][nx]:
                    break
                if game_map[ny][nx] == stone:
                    is_good_2_flip = True
                    break
                stone_2_flip.append((ny, nx))
                ny += dy[d]
                nx += dx[d]
            if is_good_2_flip:
                for stone_pos in stone_2_flip:
                    game_map[stone_pos[0]][stone_pos[1]] = stone

    for row in game_map:
        print(*row)
    print()


for tc in range(int(input())):
    N, M = map(int, input().split())
    game_map = [[0] * N for _ in range(N)]
    init_game()
    for _ in range(M):
        data = list(map(int, input().split()))
        put_stone(data[1], data[0], data[2])
    black = 0
    white = 0
    for y in range(N):
        for x in range(N):
            if game_map[y][x] == 1:
                black += 1
            elif game_map[y][x] == 2:
                white += 1
    print(f"#{tc+1}", black, white)
