n, k = map(int, input().split())
calc_cnt = 0

while n != 1:

    calc_cnt += 1

    if n % k == 0:
        n /= k
    else:
        n -= 1

print(calc_cnt)
