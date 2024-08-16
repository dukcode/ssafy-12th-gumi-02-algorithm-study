T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = 0
    min_num = 0
    for i in range(N):
        if numbers[max_num] <= numbers[i]:
            max_num = i
        if numbers[min_num] > numbers[i]:
            min_num = i
    if max_num > min_num:
        result = max_num - min_num
    if min_num > max_num:
        result = min_num - max_num
    print(f'#{tc} {result}')
