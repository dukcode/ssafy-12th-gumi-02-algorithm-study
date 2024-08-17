# 돌 뒤집기 게임


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

    # 5,3 이면 5번째부터 5,6,7까지
    # 근데 인덱스 상으로는 1이 빠져야됨
    # 다행인건 for문에서 1씩 빼준다 개이득
        if lst[i-1] == 1:
            for x in range(j):
                if i+x-1 >= N:
                    break
                lst[i+x-1] = 1
        elif lst[i-1] == 0:
            for x in range(j):
                if i+x-1 >= N:
                    break
                lst[i+x-1] = 0


    print(f'#{tc}', *lst)