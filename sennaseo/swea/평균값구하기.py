T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    sum_arr = 0
    for i in range(10):
        sum_arr += arr[i]
    average = sum_arr / 10
    if average - int(average) >= 0.5:
        result = int(average) + 1
    else:
        result = int(average)
    print(f'#{tc} {result}')