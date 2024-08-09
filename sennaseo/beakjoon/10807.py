# 첫째줄에 정수의 개수가 주어진다
# 둘째줄에는 정수가 공백으로 구분되어져 있다
# 셋째줄에는 찾으려고 하는 정수 v가 주어진다
# T개의 정수가 주어졌을때 정수 v가 몇개인지
T = int(input())
data = map(int,input().split())
v = int(input())
number_of_v = []
for x in data:
    if v == x:
        number_of_v.append(x)
print(len(number_of_v))

# T = int(input())
# data = map(int,input().split())
# v = int(input())
# count = 0
# for x in data:
#     if v == x:
#         count += 1
# print(count)

# count += 1을 통해 더 쉽게 할 수 있었다