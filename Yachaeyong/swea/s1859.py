# import sys
#
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    ans = 0
    max_price = price[-1]

    for i in range(len(price)-1, -1, -1):
        if max_price < price[i]:
            max_price = price[i]
            continue

        ans += (max_price - price[i])
    print(f'#{tc} {ans}')

    # # 원래 내가 생각했던 로직
    # # 가장 안 비쌀때 사서 가장 비쌀때 다 팔기
    # def solve(data):
    #     ret = 0
    #     start = 0
    #
    #     while start < N:
    #         max_idx = start
    #         for i in range(start, N):
    #             if data[i] >= data[max_idx]:
    #                 max_idx = i
    #
    #         for i in range(start, max_idx):
    #             ret += data[max_idx] - data[i]
    #
    #         start = max_idx + 1
    #
    #     return ret
    #
    # print(f'#{tc} {solve(price)}')

