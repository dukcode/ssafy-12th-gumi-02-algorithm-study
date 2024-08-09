def is_progressive(num):
    digit = 10
    while num != 0:
        if digit < (num % 10):
            return False
        digit = num % 10
        num //= 10
    return True


t = int(input())
for ts in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = -1
    for i in range(len(arr)):
        left = arr[i]
        for j in range(i + 1, len(arr)):
            right = arr[j]
            if is_progressive(left * right):
                ans = max(ans, left * right)

    print(f"#{ts} {ans}")
