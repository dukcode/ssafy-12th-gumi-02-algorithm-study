for tc in range(int(input())):
    ans = 0
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    def get_score(power, init_y, init_x):
        score_1 = 0
        score_2 = 0
        way_1 = ((y, x) for y in range(-power + 1, power) for x in range(-power + 1, power) if
                 abs(y) == abs(x))
        way_2 = ((y, x) for y in range(-power + 1, power) for x in range(-power + 1, power) if
                 y == 0 or x == 0)
        
        for direction_1 in way_1:
            idx_y = init_y + direction_1[0]
            idx_x = init_x + direction_1[1]
            if 0 <= idx_y < N and 0 <= idx_x < N:
                score_1 += matrix[idx_y][idx_x]

        for direction_2 in way_2:
            idx_y = init_y + direction_2[0]
            idx_x = init_x + direction_2[1]
            if 0 <= idx_y < N and 0 <= idx_x < N:
                score_2 += matrix[idx_y][idx_x]

        return max(score_1, score_2)

    for y in range(N):
        for x in range(N):
            score = get_score(M, y, x)
            ans = max(ans, score)

    print(f'#{tc + 1} {ans}')
