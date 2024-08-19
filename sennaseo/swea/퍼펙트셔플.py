T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    result = [0] * N
    a = 0
    for b in range((N // 2)+(N % 2)):
        result[a] = arr[b]
        a += 2
    a = 0
    for c in range((N // 2)+(N % 2), N):
        result[a+1] = arr[c]
        a += 2
    print(f'#{tc}', ' '.join(result))