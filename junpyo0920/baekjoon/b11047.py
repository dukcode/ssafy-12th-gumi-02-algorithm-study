n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

# total = 0
# cnt = 0
#
# while total != k:
#     for c in arr:
#         if total + c <= k:
#             total += c
#             cnt += 1
#             break
#
# print(cnt)

cnt = 0
idx = 0

while k != 0:
    cnt += k // arr[idx]
    k %= arr[idx]
    idx += 1

print(cnt)
