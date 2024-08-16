T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            kill_sum = 0
            for i in range(M):
                for j in range(M):
                    kill_sum += arr[r + i][c + j]
            if max_kill < kill_sum:
                max_kill = kill_sum
    # 위나 아래나 답 나오는 거는 맞는데 더 편한거 찾아가면서 해봐라
    # for r in range(N - M + 1):
    #     for c in range(N - M + 1):
    #         for i in range(r, r + M):
    #             for j in range(c, c + M):
    #                 arr[i][j]
    print(f'#{tc} {max_kill}')
