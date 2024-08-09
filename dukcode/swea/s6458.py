t = int(input())
for tc in range(1, t + 1):
    arr = [0] * 5000

    n = int(input())
    for _ in range(n):
        a, b = tuple(map(int, input().split()))
        for i in range(a, b + 1):
            arr[i - 1] += 1

    p = int(input())
    ans = []
    for _ in range(p):
        i = int(input())
        ans.append(arr[i - 1])

    print(f"#{tc} ", end="")
    print(" ".join(map(str, ans)))
