N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[N - 1]
second = arr[N - 2]

ans = 0
while True:
    for _ in range(K):
        if M == 0:
            break
        ans += first
        M -= 1
    if M == 0:
        break
    ans += second
    M -= 1
print(ans)
