def sudoku(arr):
    is_ok = True
    # 행
    for r in range(9):
        check = []
        for c in range(9):
            if arr[r][c] not in check:
                check.append(arr[r][c])
        if len(check) != 9:
            is_ok = False
            break
    # 열
    for r in range(9):
        check = []
        for c in range(9):
            if arr[c][r] not in check:
                check.append(arr[c][r])
        if len(check) != 9:
            is_ok = False
            break
    # 작은 격자
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            check = []
            for i in range(3):
                for j in range(3):
                    if arr[r+i][c+j] not in check:
                        check.append(arr[r+i][c+j])
            if len(check) != 9:
                is_ok = False
                break

    if is_ok:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {sudoku(arr)}')