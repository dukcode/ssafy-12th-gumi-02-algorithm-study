di = [0, 1, 0, -1]  # 상하좌우 
dj = [1, 0, -1, 0]

T = int(input())  

for tc in range(1, T + 1):
    n = int(input())  
    arr = [list(map(int, input().split())) for _ in range(n)]  #
    
    # 경비원(2) 찾기 및 상하좌우 탐색
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:  # 경비원 위치 발견
                for k in range(4):  # 상하좌우 탐색
                    ni, nj = i, j  # 현재 경비원 위치에서 출발
                    while True:
                        ni += di[k]  # 상하좌우 방향으로 이동
                        nj += dj[k]
                        if 0 <= ni < n and 0 <= nj < n:  # 배열 범위 내에 있는지 확인
                            if arr[ni][nj] == 1:  # 벽을 만나면 그 방향으로의 탐색 중단
                                break
                            elif arr[ni][nj] == 0:  # 감시 가능 구역(0) 발견 시 -1로 변경
                                arr[ni][nj] = -1
                        else:
                            break  # 배열 범위를 벗어나면 탐색 중단
    
    # 감시되지 않은 사각지대(0)의 갯수 세기
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1
    
    # 결과 출력
    print(f'#{tc} {cnt}')
