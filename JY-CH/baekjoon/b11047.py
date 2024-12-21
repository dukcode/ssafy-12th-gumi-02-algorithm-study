# 동전 0

import sys
input = sys.stdin.readline

def check(data, k):
    cnt = 0
    while True:
        for i in range(len(data)):
           cnt += k // data[i]
           k -= (k // data[i]) * data[i]
           if k == 0:
               return cnt
            

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.reverse()
print(check(data, k))
