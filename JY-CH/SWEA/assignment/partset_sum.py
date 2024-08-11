# 부분집합 합합
a = [i for i in range(1,13)]
m = len(a)
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())

    result = 0

    for i in range(1 << m):
        cnt = 0
        set_sum = 0
        for j in range(m):
            if i & (1 << j):
                cnt += 1
                set_sum += a[j]
        if cnt == n and set_sum == k:
            result += 1

    print(f'#{tc} {result}')
