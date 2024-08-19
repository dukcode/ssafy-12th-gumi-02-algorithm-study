# 최빈수 구하기

T = int(input())
for _ in range(1, T+1):
    tc = int(input())
    num = list(map(int, input().split()))


    count = [0] * (len(num) + 1)
    for i in num:
        count[i] += 1

    max_idx = count.index(max(count))
    for i in range(len(count)):
        if count[max_idx] <= count[i]:
            if max_idx < i:
                max_idx = i


    print(f'#{tc} {max_idx}')





