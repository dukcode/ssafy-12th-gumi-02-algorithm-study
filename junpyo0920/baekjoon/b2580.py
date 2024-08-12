# https://www.acmicpc.net/problem/2580
# 계속 시간 초과 떠서 결국 python으로는 못 풀고 pypy로 해결
#   - input() -> sys.stdin.readline() 으로 바꾸기
#   - python3 -> pypy3 로 바꾸기
# 정답이 여러 개인 경우 정답 하나 출력 후 종료해야 함
#   - quit() 떠서 종료 시킴
import sys


# 같은 row에 넣으려는 숫자 있는지 확인
def is_num_in_row(y, num):
    if num in sudoku[y]:
        return True
    return False


# 같은 column에 넣으려는 숫자 있는지 확인
def is_num_in_col(x, num):
    for y in range(9):
        if sudoku[y][x] == num:
            return True
    return False


# 같은 area(3 x 3)에 넣으려는 숫자 있는지 확인
def is_num_in_area(x, y, num):
    s_y = (y // 3) * 3
    s_x = (x // 3) * 3
    for y in range(s_y, s_y+3):
        for x in range(s_x, s_x+3):
            if sudoku[y][x] == num:
                return True
    return False


# 빈 공간에 숫자 넣어보기
def put_num(idx_b):
    # 모든 빈 칸 확인 완료
    if idx_b == len(blanks):
        for row in sudoku:
            print(*row)
        # 아예 종료 시켜야 오답 처리 안 됨
        quit()

    # 빈 칸에 1~10 넣어보기
    for num in range(1, 10):
        blank = blanks[idx_b]
        # num이 같은 열, 행, 공간에 없으면
        if not is_num_in_row(blank[0], num) and not is_num_in_col(blank[1], num) and not is_num_in_area(blank[1], blank[0], num):
            sudoku[blank[0]][blank[1]] = num
            put_num(idx_b+1)
            sudoku[blank[0]][blank[1]] = 0


sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blanks = []
for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            blanks.append((i, j))
put_num(0)