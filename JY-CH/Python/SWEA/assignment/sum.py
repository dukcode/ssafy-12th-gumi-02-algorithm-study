# sum

for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0

    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
        if max_sum < row_sum:
            max_sum = row_sum

    for j in range(100):
        colone_sum = 0
        for i in range(100):
            colone_sum += arr[i][j]
        if max_sum < colone_sum:
            max_sum = colone_sum


    stair_sum = 0
    i, j = 0, 0
    for _ in range(100):
        stair_sum += arr[i][j]
        i += 1
        j += 1
    if max_sum < stair_sum:
        max_sum = stair_sum

    rev_stair_sum = 0
    i, j = 0, 99
    for _ in range(100):
        rev_stair_sum += arr[i][j]
        i += 1
        j -= 1
    if max_sum < rev_stair_sum:
        max_sum = rev_stair_sum

    print(f'#{tc} {max_sum}')

