#최대 최소의 간격

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0

    for i in range(N):
        if lst[max_idx] <= lst[i]:
            max_idx = i

        if lst[min_idx] > lst[i]:
            min_idx = i

    print(f'#{tc} {abs(max_idx - min_idx)}')
