def fibonacci(n):
    if n == 0:
        memo[0] = (1, 0)
        return
    elif n == 1:
        memo[1] = (0, 1)
        return
    elif memo[n-2] and memo[n-1]:
        memo[n] = (memo[n - 1][0] + memo[n - 2][0], memo[n - 1][1] + memo[n - 2][1])
        return
    else:
        fibonacci(n - 2)
        fibonacci(n - 1)
        memo[n] = (memo[n - 1][0] + memo[n - 2][0], memo[n - 1][1] + memo[n - 2][1])
        return


memo = [tuple()] * 41
for tc in range(int(input())):
    n = int(input())
    fibonacci(n)
    print(*memo[n])
