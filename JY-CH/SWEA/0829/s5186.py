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


    print(x, y)
    print(arr[x][y-55:y+1])

    for i in range(0,56,7):
        check_lst=[]
        for j in range(7):
            check_lst.append(arr[x][(y-55) + i+j])

        key = ''.join(map(str, check_lst))










