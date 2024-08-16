T = int(input())

for _ in range(1, T + 1):
    tc = int(input())
    score = list(map(int, input().split()))

    cnt = [0] * 101
    N = len(score)
    M = len(cnt)
    for i in range(N):
        cnt[score[i]] += 1
    max_v = 0
    idx = 0

    for i in range(M):
        if max_v <= cnt[i]:
            max_v = cnt[i]
            idx = i

    print(f'#{tc} {idx}')
