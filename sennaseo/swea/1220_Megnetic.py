for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    cnt = 0 # 테이블 위에 남아있는 교착상태의 수
 
    for i in range(N):
        meg = 0
        for j in range(N):
            if arr[j][i] == 1: # 좌표값이 N극 자성체일 시 meg = 1
                meg = 1
            if meg == 1 and arr[j][i] == 2: # N극 자성체일때 S극 자성체를 돌며 찾음
                cnt += 1 # 찾았을시 cnt + 1
                meg = 0 # meg는 다시 리셋
 
    print(f'#{tc} {cnt}')