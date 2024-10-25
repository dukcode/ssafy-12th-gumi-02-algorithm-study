# 신입 사원
import sys

T = int(input())
for _ in range(T):
    N = int(input())
    ranking = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    ranking.sort()

    cnt = 1
    cut_line = 0
    for i in range(1, N):
        if ranking[i][1] < ranking[cut_line][1]:
            cnt += 1
            cut_line = i
    print(cnt)
