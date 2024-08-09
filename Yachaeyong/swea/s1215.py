N = 8

for tc in range(1, 11):
    M = int(input())
    arr = [list(map(str, input().strip())) for _ in range(N)]
    cnt = 0

    # 행
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - 1 - k]:
                    break
            else:
                cnt += 1
    # 열
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if arr[j + k][i] != arr[j + M - 1 - k][i]:
                    break
            else:
                cnt += 1

    print(f'#{tc} {cnt}')
