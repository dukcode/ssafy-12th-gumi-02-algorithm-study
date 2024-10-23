# 신입 사원
import sys

T = int(input())
for _ in range(T):
    N = int(input())
    ranking = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    ranking.sort(key=lambda x: -x[0])

    cnt = 0
    for f in range(N):
        for s in range(f + 1, N):
            if ranking[f][0] < ranking[s][0] and ranking[f][1] < ranking[s][1]:
                cnt += 1
                break
    ans = N - cnt
    print(ans)
