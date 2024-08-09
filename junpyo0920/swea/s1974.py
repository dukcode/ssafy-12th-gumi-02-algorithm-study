for test_case in range(int(input())):
    ans = '1'
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    def validate(line):
        return len(set(line)) == 9

    area_checker = (0, 3, 6)
    
    for y in range(9):
        row = sudoku[y]
        col = []
        area = []
        for x in range(9):
            col.append(sudoku[x][y])

            if (y in area_checker) and (x in area_checker):
                for y_2 in range(3):
                    for x_2 in range(3):
                        area.append(sudoku[y + y_2][x + x_2])
                if not validate(area): ans = '0'
                area = []
            
        if not (validate(row) and validate(col) and ans == '1'):
            ans = '0'
        else:
            ans = '1'
            

    print(f'#{test_case + 1} {ans}')
