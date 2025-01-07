T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    result2 = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            # 진짜 여기가 제일 중요함
            # 0 만났는데 cnt가 k면
            # 바로 값에 +1
            # 아니면 cnt 리셋
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    for i in range(N):
        cnt2 = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt2 += 1
            else:
                if cnt2 == K:
                    result2 += 1
                cnt2 = 0
        if cnt2 == K:
            result2 += 1
    print(f'#{tc} {result+result2}')
