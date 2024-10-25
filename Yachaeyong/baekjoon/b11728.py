# 배열 합치기
import sys

N, M = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
ans = A+B
ans.sort()
# ans = sorted(A+B)
print(*ans)
