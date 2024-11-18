# 에라토스테네스의 체

N, K = map(int, input().split())
tmp = 0
sieve = [True] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if sieve[j] != False:
            sieve[j] = False
            tmp += 1
            if tmp == K:
                print(j)
