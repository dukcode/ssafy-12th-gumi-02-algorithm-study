# 영화감독 숌

import sys
input = sys.stdin.readline

def find_num(n):
    cnt = 0
    number = 666

    while True:
        if '666' in str(number):
            cnt += 1
            if cnt == n:
                return number
        
        number += 1


n = int(input())
print(find_num(n))

