# 1220. Magnetic

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = []
    for i in range(N):
        temp = []
        for j in range(N):
            if arr[j][i] != 0:
                temp.append(arr[j][i])
        check.append(temp)

    cnt = 0
    for line in check:
        for i in range(len(line) - 1):
            if line[i] == 1 and line[i + 1] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')
