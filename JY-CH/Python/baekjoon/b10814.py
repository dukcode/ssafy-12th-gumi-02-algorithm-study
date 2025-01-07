# 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
data = []
for idx in range(n):
    data.append(tuple(input().split()))


result = sorted(data, key=lambda x: (int(x[0])))

for i in range(n):
    print(f'{result[i][0]} {result[i][1]}')

# 오 나 튜플이랑 람다 다써봄 오오
# 오오오오오옹