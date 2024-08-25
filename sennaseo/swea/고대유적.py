T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    
    result = 0
    for i in range(N):
        row_add = 0
        for j in range(M):
            if arr[i][j] == 1: # 만약 가로줄에 있는 구조물을 찾으면
                row_add += 1 # row_add에 +1
            elif arr[i][j] == 0: # 만약 빈땅을 만나게 되면
                if result < row_add: # 그 즉시 바로 구조물의 수를 최고값과 비교
                    result = row_add # 만약 최고값보다 크다면 값 바꾸기
                row_add = 0 # 그리고 빈땅을 만났기 때문에 리셋

            if j == M -1 and result < row_add: # 가로줄 끝에 다다랐다면 최고값과 비교
                result = row_add # 만약 최고값보다 크다면 값 바꾸기
    
    for i in range(M): # 세로줄도 가로줄과 같은 로직으로 탐색함
        column_add = 0
        for j in range(N):
            if arr[j][i] == 1:
                column_add += 1
            elif arr[j][i] == 0:
                if result < column_add:
                    result = column_add
                column_add = 0

            if j == N -1 and result < column_add:
                result = column_add

    print(f'#{tc} {result}') # 계속 비교해서 가장 큰 값이 result

