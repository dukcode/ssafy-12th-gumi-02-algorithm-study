# 팩토리얼 0의 개수

import sys
input = sys.stdin.readline

n = int(input())

# 5 10 15 20 25 30 35
# 5 1개당 0이 갯수가 +1 인데
# 25를 어케 처리함

cnt = 0
while n >= 5:
    cnt += n // 5
    n //= 5

print(cnt)