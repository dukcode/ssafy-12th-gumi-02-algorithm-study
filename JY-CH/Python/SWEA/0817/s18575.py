# 풍선팡 보너스 게임

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    value_list = []
    for i in range(N):
        for j in range(N):
            value = arr[i][j]
            for k in range(4):
                for l in range(1, N+1):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l

                    if 0 <= ni < N and 0 <= nj < N:
                        value += arr[ni][nj]

            value_list.append(value)

    result = (max(sorted(value_list)) - min(sorted(value_list)))
    print(f'#{tc} {result}')

    # second_value = 0
    # for i in range(N):
    #     for j in range(N):
    #
    #         value = arr[i][j]
    #         for k in range(4):
    #             for l in range(1, arr[i][j] + 1):
    #                 ni = i + di[k] * l
    #                 nj = j + dj[k] * l
    #
    #                 if 0 <= ni < N and 0 <= nj < N:
    #                     value += arr[ni][nj]
    #
    #         if min_value > value:
    #             min_value = value
    #
    #
    # print(min_value)





