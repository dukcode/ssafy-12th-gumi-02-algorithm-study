for tc in range(int(input())):
    ans = 0
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    def get_score(y, x):
        score = matrix[y][x]
        move = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for direction in move:
            if y + direction[0] >= 0 and x + direction[1] >= 0 and y + direction[0] < N and x + direction[1] < M:
                score += matrix[y+direction[0]][x+direction[1]]
        return score

    for y in range(N):
        for x in range(M):
            score = get_score(y,x)
            if score > ans: ans = score
    
    print(f'#{tc+1} {ans}')