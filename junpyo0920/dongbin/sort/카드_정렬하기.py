from heapq import heappop, heappush, heapify

# 3트
n = int(input())
arr = [int(input()) for _ in range(n)]
heapify(arr)

ans = 0
while len(arr) > 1:
    new_cards = heappop(arr) + heappop(arr)
    ans += new_cards
    heappush(arr, new_cards)

print(ans)


# 1트
# n = int(input())
# arr = [int(input()) for _ in range(n)]
# arr.sort()
# ans = 0
# print(ans)
#
# memo = [arr[0]]
# ans = 0
# for i in range(1, n):
#     ans += memo[i - 1] + arr[i]
#     memo.append(memo[i - 1] + arr[i])
# print(ans)

# 2트
# def divide(s, e):
#     global ans
#     if s >= e:
#         return arr[s]
#
#     half = (s + e) // 2
#     left = divide(s, half)
#     right = divide(half + 1, e)
#
#     ans += left + right
#     return left + right
