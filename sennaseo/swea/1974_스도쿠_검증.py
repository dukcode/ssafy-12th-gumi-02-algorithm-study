T = int(input())
for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    answer = 1

    for i in range(9):
        for j in range(8):
            for k in range(j+1, 9):
                # row
                if puzzle[i][j] == puzzle[i][k]:
                    answer = 0
                # column
                if puzzle[j][i] == puzzle[k][i]:
                    answer = 0
    # square
    for a in range(0, 9, 3):
        for b in range(0, 9, 3):
            save = []
            for c in range(a, a + 3):
                for d in range(b, b + 3):
                    save.append(puzzle[c][d])

            for z in range(8):
                for y in range(z+1, 9):
                    if save[z] == save[y]:
                        answer = 0

    print(f'#{tc} {answer}')