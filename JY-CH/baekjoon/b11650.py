# 좌표 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))

# data = [tuple(map(int, input().split())) for _ in range(n)]
# 한줄로 줄일 수 있다. 잊지말자.

data = sorted(data, key=lambda x: (x[0], x[1]))

for i in range(n):
    print(f'{data[i][0]} {data[i][1]}')