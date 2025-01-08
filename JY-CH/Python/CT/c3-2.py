# 큰 수의 법칙

N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num1 = sorted(num)

max1 = num1[-1]
max2 = num1[-2]

cnt = 0
cnt2 = 0
while M > 2*K:
    cnt += 1
    M -= 2*K
    if M < 2*K:
        cnt2 = M

result = (max1 * cnt * 2*K) + (max2 * cnt2)

print(result)

