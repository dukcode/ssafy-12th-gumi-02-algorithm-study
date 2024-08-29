# 단순 이진 암호코드

pass_dict = {'0001101' : 0,
                 '0011001' : 1,
                 '0010011' : 2,
                 '0111101' : 3,
                 '0100011' : 4,
                 '0110001' : 5,
                 '0101111' : 6,
                 '0111011' : 7,
                 '0110111' : 8,
                 '0001011' : 9}



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]


    x = 0
    y = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                x ,y = i, j

    answer_lst=[]
    for i in range(0,56,7):
        check_lst=[]
        for j in range(7):
            check_lst.append(arr[x][(y-55) + i+j])

        key = ''.join(map(str, check_lst))
        answer_lst.append(pass_dict[f'{key}'])

    sum1 = 0
    sum2 = 0
    for i in range(0, 8, 2):
        sum1 += answer_lst[i]*3
        sum2 += answer_lst[i+1]

    result = sum1 + sum2
    if result % 10 == 0:
        print(f'#{tc} {sum(answer_lst)}')
    else:
        print(f'#{tc} {0}')


