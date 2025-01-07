# 1로 만들기
import sys
input = sys.stdin.readline


# 틀림
# 6 넣으면 갇힘
# def make_one(x, cnt):
#     if x % 3 == 0:
#         cnt += 1
#         x = x // 3
#         if x == 1:
#             return cnt
#         else:
#             return make_one(x, cnt)
#     elif x % 3 == 1:
#         cnt += 1
#         x = x - 1
#         if x == 1:
#             return cnt
#         else:
#             return make_one(x, cnt)
#     elif x % 3 == 2:
#         if x // 2 == 1:
#             cnt += 1
#             return cnt
#         else:
#             cnt += 2
#             x = x - 2
#             if x == 1:
#                 return cnt
#             else:
#                 return make_one(x, cnt)


# dp를 이용
# 결국 쓰던 값을 반복해서 쓰는거니까? dp를 했어야됬다.
# dp에 해당하는 것은 최소 연산 횟수
def make_one(n):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # 3번 조건
        dp[i] = dp[i - 1] + 1

        # 2번 조건
        if i % 2 == 0:
            # 2로 나누어 떨어지면, 지금의 횟수와 2로 나누었을때의 숫자 횟수에서 + 1을 하고
            # 비교하여 낮은것을 최소 연산 횟수로 할당.
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 1번 조건
        if i % 3 == 0:
            # 3으로 나누어 떨어지면, 지금의 횟수와 3으로 나누었을때의 숫자 횟수에서 + 1을 하고
            # 비교하여 낮은것을 최소 연산 횟수로 할당.
            dp[i] = min(dp[i], dp[i // 3] + 1)

# 예시
# dp[1] = 0
# dp[2] = min(dp[2], dp[1] + 1) = 1
# dp[3] = min(dp[2], dp[1] + 1) = min(1, 0) + 1 = 1
# dp[4] = min(dp[3], dp[2] + 1) = min(1, 1) + 1 = 2
# dp[5] = dp[4] + 1 = 3

    return dp[n]




n = int(input())
cnt = make_one(n)
print(cnt)