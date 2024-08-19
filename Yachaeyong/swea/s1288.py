# 1288 새로운 불면증 치료법
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N = list(input().strip())

    check = []
    cnt = 0
    while len(check) < 10:
        cnt += 1
        arr = list(str(N * cnt).strip())
        for i in range(len(arr)):
            if arr[i] not in check:
                check.append(arr[i])

    ans = N * cnt
    print(f'#{tc} {ans}')
