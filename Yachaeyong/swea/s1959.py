# 1959 두 개의 숫자열

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_v = 0
    # A < B
    if N < M:
        for i in range(M - N + 1):
            sum_mul = 0
            for j in range(N):
                sum_mul += A[j] * B[i+j]
            if max_v < sum_mul:
                max_v = sum_mul
    # A > B
    elif N > M:
        for i in range(N - M + 1):
            sum_mul = 0
            for j in range(M):
                sum_mul += A[i+j] * B[j]
            if max_v < sum_mul:
                max_v = sum_mul

    print(f'#{tc} {max_v}')