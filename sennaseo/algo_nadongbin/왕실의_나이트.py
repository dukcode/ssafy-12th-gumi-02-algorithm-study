direction = input()
row = int(direction[1])
column = int(ord(direction[0])) - int(ord("a")) + 1

STEPS = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in STEPS:
    row_direction = row + step[1]
    column_direction = column + step[0]
    if (
        row_direction >= 1
        and row_direction <= 8
        and column_direction >= 1
        and column_direction <= 8
    ):
        result += 1
print(result)

# 인덱스값이 아니라 움직임이 가능한 range가 1부터 8이므로 인덱스와 상관 없음
# 인덱스 값과 주어진 range를 헷갈리지 말자
