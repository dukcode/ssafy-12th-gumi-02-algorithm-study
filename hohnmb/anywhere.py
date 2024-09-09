T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 5 3
    # white = 1
    # black = 0
    result = 0
    # 가로
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 1:  # 빈칸이면
                cnt += 1

            else:  # 빈칸이 아니면
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:  # 빈칸이면
                cnt += 1
            else:  # 빈칸이 아니면
                if cnt == k:
                    result += 1
                cnt = 0
        if cnt == k:
            result += 1

    print(f'#{tc} {result}')

# 0 0 1 1 1
# 1 1 1 1 0
# 0 0 1 0 0
# 0 1 1 1 1
# 1 1 1 0 1

# arr[0][0] [0][1] [0][2]
# arr[0][1] [0][2] [0][3]

# 0 2 0 3 0 4
# 1 2 1 3 1 4
