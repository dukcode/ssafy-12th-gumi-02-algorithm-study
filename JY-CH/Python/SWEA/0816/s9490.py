# 풍선팡!
di = [0,1,0,-1]
dj = [1,0,-1,0]



T = int(input())
for tc in range (1, T+1):
    N, M = map(int, input().split()) # 행, 열 크기
    arr = [list(map(int, input().split())) for _ in range(N)] # 풍선별 꽃가루 수

    max_v = 0   # 꽃가루 최대 합계
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j] # 터트린 풍선에서 나오는 꽃가루 개수
            # 주변 풍선의 꽃가루 수
            for k in range(4): # 확인할 방향
                for l in range(1, arr[i][j]+1):   # 주변방향으로 추가로 터지는 풍선과의 거리
                    ni = i + di[k]*l

