T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    is_true=True
    #가로
    for i in range(9):
        total = 45
        for j in range(9):
            total -= arr[i][j]
        if total != 0:
            is_true=False
    #세로
    for k in range(9):
        total = 45
        for l in range(9):
            total -= arr[l][k]
        if total != 0:
            is_true=False
    #3*3
    for m in range(0,9,3):
        for n in range(0,9,3):
            total = 45
            for i in range(m,m+3):
                for j in range(n,n+3):
                    total -= arr[i][j]
            if total != 0:
                is_true=False
    if is_true ==False:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')





