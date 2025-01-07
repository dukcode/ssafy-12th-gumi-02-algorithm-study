# min, max

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

# 최대값, 최소값 찾기
    max_value = numbers[0]
    min_value = numbers[0]
    # numbers를 하나 하나 보기
    for i in range(N):
        if numbers[i] > max_value:
            max_value = numbers[i]
        
        elif numbers[i] < min_value:
            min_value = numbers[i]
    print(f'#{tc} {max_value - min_value}')