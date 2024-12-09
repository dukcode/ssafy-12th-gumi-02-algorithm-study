# 수 정렬하기 2
import sys
input = sys.stdin.readline


n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

for i in data:
    print(i)


# n = int(input())
# data = [0] * 1000001
# minus_data = [0] * 1000000
# for _ in range(n):
#     x = int(input())
#     if x >= 0:
#         data[x] += 1
#     else:
#         minus_data[-x] += 1

# for i in range(len(minus_data) - 1, -1 , -1):
#     if minus_data[i]:
#         print(-i)

# for j in range(len(data)):
#     if data[j]:
#         print(j)
