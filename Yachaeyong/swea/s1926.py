# 간단한 369

N = int(input())

num = [str(i) for i in range(1, N + 1)]

for i in num:
    cnt = 0
    for j in i:
        if j in '369':
            cnt += 1
    if cnt == 0:
        print(i, end=' ')
    else:
        print('-' * cnt, end=' ')