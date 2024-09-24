T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # 5, 4
    result = 0
    # 가로
    for i in range(n):# 5
        cnt = 0
        for j in range(m):# 4
            if arr[i][j] == 1:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                cnt = 0
    for i in range(m):# 5
        cnt = 0
        for j in range(n):# 4
            if arr[j][i] == 1:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                cnt = 0

    print(f'#{tc} {result}')
