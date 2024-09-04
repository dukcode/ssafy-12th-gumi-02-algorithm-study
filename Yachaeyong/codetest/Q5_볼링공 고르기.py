# 볼링공 고르기
N, M = map(int, input().split())

balls = list(map(int, input().split()))

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if balls[i] != balls[j]:
            cnt += 1

print(cnt)

# count = [0] * 11
# for ball in balls:
#     count[ball] += 1
#
# ans = 0
# for i in range(1, M+1):
#     N -= count[i]
#     ans += count[i] * N
#
# print(ans)