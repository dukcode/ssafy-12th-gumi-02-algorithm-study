# 보물
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
S = 0
for i in range(N):
    max_B = max(B)
    S += A[i] * max_B
    B.remove(max_B)

print(S)

# # B 정렬한 방법
# temp = []
# for i in range(N):
#     temp.append((B[i], i))
#
# A.sort()
# temp.sort(key=lambda x: -x[0])
#
# S = 0
# for i in range(N):
#     S += A[i] * temp[i][0]

# print(S)
