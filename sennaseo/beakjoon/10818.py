# N개의 정수의 갯수가 주어진다
# 둘째줄에는 N개의 정수를 공백으로 구분해서 주어진다.
N = int(input())
data = map(int,input().split())

min_max = []
for x in data:
    min_max.append(x)
print(min(min_max), max(min_max))