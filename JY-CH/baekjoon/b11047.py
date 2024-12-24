# 동전 0

import sys
input = sys.stdin.readline

# 그리디 드가자아!
def check(data, k):
    cnt = 0
    while True:
        for i in range(len(data)):
           cnt += k // data[i]
           k -= (k // data[i]) * data[i]
           if k == 0:
               return cnt
            

n, k = map(int, input().split())
# 그리디!
data = []
for _ in range(n):
    data.append(int(input()))

data.reverse()
print(check(data, k))
