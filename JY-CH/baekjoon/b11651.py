# 좌표 정렬하기2
import sys
input = sys.stdin.readline



n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]

data = sorted(data, key=lambda x: (x[1], x[0]))

for i in range(n):
    print(f'{data[i][0]} {data[i][1]}')