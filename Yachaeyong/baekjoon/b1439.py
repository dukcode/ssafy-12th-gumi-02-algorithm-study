# 뒤집기
import sys

S = sys.stdin.readline().rstrip()

cnt = 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        cnt += 1

print((cnt+1)//2)