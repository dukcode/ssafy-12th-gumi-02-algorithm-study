# 점점 커지는 당근의 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    # 당근 카운트용
    cnt = 1
    fixed_cnt = 1
    for i in range(1, N):
        # 커지면 카운트 올린다.
        if carrot[i-1] < carrot[i]:
            cnt += 1
            # 고정 카운트보다 크면 바꾼다.
            if fixed_cnt < cnt:
                fixed_cnt = cnt
        # 이게 제일 중요하다.
        # 아니면 초기화 시켜야된다.
        else:
            cnt = 1


    print(f'#{tc} {fixed_cnt}')