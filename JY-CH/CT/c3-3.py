# 숫자 카드 게임
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    result = 0
    for i in range(N):
        temp = 99999
        for j in range(M):
            if arr[i][j] < temp:
                temp = arr[i][j]

        if result < temp:
            result = temp

    print(f'#{tc} {result}')


# 일일이 체크하려니 귀찮아서 swea식으로 변형시킴.


