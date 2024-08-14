# 요세푸스 문제

from collections import deque

N, K = map(int, input().split())

people = deque()
for i in range(1, N+1):
    people.append(i)

result = []

while people:
    for _ in range(K-1):
        people.append(people.popleft())
    result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))
# #-----------------------------------------------------#
# N, K = map(int, input().split())
# arr = [i for i in range(1, N+1)]
# num = 0
# result = []
# for _ in range(N):
#     num += K-1
#     if num >= len(arr):
#         num %= len(arr)
#     result.append(str(arr[num]))
#     arr.pop(num)

# print(result)
