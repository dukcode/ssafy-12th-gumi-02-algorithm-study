# 기타줄

N, M = map(int, input().split())

bundle = []
each = []
for _ in range(M):
    b, e = map(int, input().split())
    bundle.append(b)
    each.append(e)

bundle.sort()
each.sort()

min_cost = int(1e9)
for b in bundle:
    b_cost = b * (N // 6 + 1)
    for e in each:
        e_cost = e * N
        mix_cost = (b * (N // 6) + e * (N % 6))
        min_cost = min(min_cost, b_cost, e_cost, mix_cost)
print(min_cost)

# min_bundle = min(bundle)
# min_each = min(each)
#
# ans = 0
# if min_bundle < min_each * 6:
#     # 묶음으로 다 사는게 더 싼 경우
#     if min_bundle < min_each * (N % 6):
#         ans = min_bundle * ((N // 6) + 1)
#     # 최대한 묶음으로 사고 남는 개수는 낱개로 사는게 싼 경우
#     else:
#         ans = min_bundle * (N // 6) + min_each * (N % 6)
# # 낱개로 다 사는게 더 싼 경우
# elif min_bundle >= min_each * 6:
#     ans = min_each * N
# print(ans)