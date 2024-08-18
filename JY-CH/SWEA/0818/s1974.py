# 스도쿠 검증

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = 1
    for i in range(9):
        check = set()
        check2 = set()
        for j in range(9):
            check.add(sudoku[i][j])
            check2.add(sudoku[j][i])
        if len(check) != 9 or len(check2) != 9:
            result = 0
            break



    dc = [0, 3, 6, 0, 3, 6, 0, 3, 6]
    dr = [0, 0, 0, 3, 3, 3, 6, 6, 6]

    for k in range(9):
        check3 = set()
        for i3 in range(3):
            for j3 in range(3):
                ni = i3 + dc[k]
                nj = j3 + dr[k]
                check3.add(sudoku[ni][nj])
        if len(check3) != 9:
            result = 0
            break


    print(f'#{tc} {result}')





