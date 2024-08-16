T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input().split()))

    total = 0
    for i in range(len(num)):
        total += num[i]

    print(f'#{tc} {round(total / 10)}')