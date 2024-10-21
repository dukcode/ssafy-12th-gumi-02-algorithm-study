# 좌표 정렬하기
import sys

input = sys.stdin.readline

N = int(input())
coordinate = [list(map(int, input().split())) for _ in range(N)]

coordinate.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*coordinate[i])
