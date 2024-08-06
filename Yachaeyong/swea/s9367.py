# 점점 커지는 당근의 개수

for tc in range(int(input())):

    N = int(input())
    C = list(map(int, input().split()))

    cnt = 0
    max_cnt = 0

    for i in range(N):
        if i == 0:
            cnt += 1
        else:
            if C[i-1] < C[i]:
                cnt += 1
            else:
                cnt = 1
        if max_cnt < cnt:
            max_cnt = cnt
   
    print(f'#{tc+1} {max_cnt}')

    