T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    add = 0
    for i in range(10):
        if arr[i] % 2 != 0:
            add += arr[i]
    print(f'#{tc} {add}')