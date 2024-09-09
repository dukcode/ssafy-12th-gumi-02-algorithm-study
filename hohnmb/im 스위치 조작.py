

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    ai = list(map(int,input().split()))
    bi = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if ai[i] != bi[i]:
            cnt += 1
            for j in range(i,n):
                ai[j] = 1 - ai[j]

    print(f'#{tc} {cnt}')



