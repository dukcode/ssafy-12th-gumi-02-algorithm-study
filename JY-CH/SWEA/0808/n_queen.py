# arr의 idx행에 모든 열에 퀸놓기



def n_queen(idx, arr, N):
    if idx == N:
        for row in arr:
            print(row)
        print('------------------')
        return
    # 정답이 될 수 없는 경우는 놓지 않기
    # 같은 열에 퀸을 놓지 않게 만들기 >> 특정열에 퀸이 놓여져 있는지 확인하는 배열
        for i in range(N):
            if not check_col[i] and not check_dia1[idx + 1] and not check_dia2[idx - i + N - 1]:    #i열에 퀸이 없으면 i열에 퀸 놓기
                arr[idx][i] = 1
                check_col[i] = 1 # i열에 퀸이 놓여짐
                check_dia1[idx + i] = 1
                check_dia2[idx - i + N - 1] = 1
                n_queen(idx + 1, arr, N)
                arr[idx][i] = 0
                check_col[i] = 0



N = 4
arr = [[0]*N for _ in range(n)]
#퀸이 놓여져 있는 열을 체크하는 배열
check_col == [0] * N
# 우 상향 대각
check_dia1 = [0] * (2*N-1)
# 우 하향 대각
check_dia2

n_queen(0, arr, N)