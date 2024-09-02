n, k = map(int, input().split())

cnt = 0
while n != 1:
    cnt += 1
    if n % k == 0:
        n /= k
        continue

    n -= 1

print(cnt)
