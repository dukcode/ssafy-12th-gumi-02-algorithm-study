T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    N = N // 10
    cnt = [0] * 31
    cnt[1] = 1
    cnt[2] = 3
    for i in range(3, 31):
        cnt[i] = cnt[i-1] + 2 * cnt[i-2]
    print(f'#{tc} {cnt[N]}')