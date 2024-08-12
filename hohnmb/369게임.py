N = int(input())

for num in range(1, N + 1):
    num = str(num)
    cnt = 0

    for val in num:
        # if val == '3' or val == '6' or val == '9':
        if val in '369':
            cnt += 1        # 카운팅

    if cnt == 0:
        print(num, end=' ')
    else:
        print('-' * cnt, end=' ')
