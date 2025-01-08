# 홀수만 더하기

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    odd_sum = 0
    for i in range(len(lst)):
        if (lst[i] % 2) == 1:
            odd_sum += lst[i]

    print(f'#{tc} {odd_sum}')