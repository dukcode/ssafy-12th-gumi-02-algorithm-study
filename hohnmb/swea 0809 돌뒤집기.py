T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    stone = list(map(int,input().split()))
    for l in range(m):
        i, j = map(int,input().split())
        i-= 1
    # 스톤에서 i번째 인덱스부터 j 거리만큼 i번째 인덱스 값으로 변한다.?
        for k in range(i, i+j):
            if k >= n:
                break
            stone[k] = stone[i]
    
    # for i in range(n):
    #  print(stone[i],end=' ')
    # # print()

    print(f'#{tc}',*stone)
            

