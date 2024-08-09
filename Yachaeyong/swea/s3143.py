def f_type(a, b):
    cnt = 0
    i = 0

    while i < N:
        if A[i:i + M] == B[:]:
            cnt += 1
            i += M
        else:
            i += 1

    return N - (M - 1) * cnt

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    N = len(A)
    M = len(B)
    ans = f_type(A, B)

    print(f'#{tc} {ans}')