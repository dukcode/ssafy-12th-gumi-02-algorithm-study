# 2^a x 3^b x 5^c x 7^d x 11^e인 수 N이 주어질 때
# a, b, c, d, e를 구하는 문제

for tc in range(1, int(input()) + 1):
    n = int(input())
    # a, b, c, d, e를 저장할 리스트
    counts = [0] * 5
    prime_nums = [2, 3, 5, 7, 11]

    # prime_nums를 순회
    for idx, prime_num in enumerate(prime_nums):
        # N이 해당 소수(prime number)로 나눌 수 없을 때까지 반복
        while n % prime_num == 0:
            # 해당 소수의 인덱스에 값을 더함
            # a: 0, b: 1, c: 2, d: 3, e: 4
            counts[idx] += 1
            # n에 n을 prime_num으로 나눈 값(== 몫, ∵ 나머지가 0인 경우에만 나누었기 때문)을 저장
            n //= prime_num
    
    print(f'#{tc}', *counts)
