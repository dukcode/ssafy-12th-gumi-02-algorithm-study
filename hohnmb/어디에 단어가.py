T = int(input())  
 
for tc in range(1, T + 1):  
    N, K = map(int, input().split())  
    arr = [list(map(int, input().split())) for _ in range(N)]  
 
    ans = 0 

    # 가로 확인
    for i in range(N):  # 각 행에 대해 반복
        count = 0  # 연속된 1의 개수를 셀 변수 초기화
        for j in range(N):  # 각 열에 대해 반복
            if arr[i][j] == 1:  # 현재 위치가 1이면
                count += 1  # 연속된 1의 개수를 증가시킴
            else:  # 현재 위치가 0이면
                if count == K:  # 지금까지 센 연속된 1의 개수가 K와 같으면
                    ans += 1  # 정답을 증가시킴
                count = 0  # 연속된 개수 초기화 (다시 시작)
        if count == K:  # 행의 끝까지 왔을 때도 연속된 개수가 K인 경우 처리
            ans += 1
 
    # 세로 확인
    for j in range(N):  # 각 열에 대해 반복
        count = 0  # 연속된 1의 개수를 셀 변수 초기화
        for i in range(N):  # 각 행에 대해 반복
            if arr[i][j] == 1:  # 현재 위치가 1이면
                count += 1  # 연속된 1의 개수를 증가시킴
            else:  # 현재 위치가 0이면
                if count == K:  # 지금까지 센 연속된 개수가 K와 같으면
                    ans += 1  # 정답을 증가시킴
                count = 0  # 연속된 개수 초기화 (다시 시작)
        if count == K:  # 열의 끝까지 왔을 때도 연속된 개수가 K인 경우 처리
            ans += 1
 
    print(f"#{tc} {ans}")  

    # 아 씨발