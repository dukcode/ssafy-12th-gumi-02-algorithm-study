# k번째 수
N = int(input())
k = int(input())

B = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        B.append(i*j)
B.sort()

start = 1
end = N * N
ans = 0
while start <= end:
    mid = (start + end) // 2

    if mid == k:
        ans = B[k]
        break
    elif mid > k:
        end = mid - 1
    else:
        start = mid + 1

print(ans)
