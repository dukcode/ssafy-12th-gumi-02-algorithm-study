T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 1000000
    # 0번부터 n - m번까지 반복하기
    for i in range(N-M+1):
        # i의 의미 : 구간 시작위치
        tmp_sum = 0
        for j in range(M):
            # 숫자를 더할 위치: i + j
            tmp_sum += numbers[i+j]
        if tmp_sum > max_sum:
            max_sum = tmp_sum

        if tmp_sum < min_sum:
            min_sum = tmp_sum
    
    print(f'#{tc} {max_sum - min_sum}')
