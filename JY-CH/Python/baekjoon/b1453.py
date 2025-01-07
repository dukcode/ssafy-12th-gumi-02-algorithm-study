# 피시방 알바 

import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

# 중복 허용 x 자리 
com_num = set()
# 카운트
cnt = 0 

for num in data:
    # 있으면 가라ㅣ
    if num in com_num:
        cnt += 1
    else:
        # 없으면 앉은거
        com_num.add(num)

print(cnt)