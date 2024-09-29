def fibonacci(n):
    cnt = 0

    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1

    for i in range(3, n + 1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]

    return f[n], cnt


n = int(input())
print(*fibonacci(n))
