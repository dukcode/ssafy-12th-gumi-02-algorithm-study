n, k = map(int, input().split())

cnt = 0

while n != 1:
    if not n % k:
        n //= k
    else:
        n -= 1
    cnt += 1

print(cnt)