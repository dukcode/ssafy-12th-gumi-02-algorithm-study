# 설탕 배달

import sys
input = sys.stdin.readline

# 5키로 3키로로 배달한다
# 안되면 -1을 출력한다
# 근데 되면 출력을 해야하는데
# 5키로 개수를 어케 조절하냐 흠

def min_cnt(n):
    # 그리디!
    for pack_5 in range(n // 5, -1, -1):
        sugar = n - (pack_5 * 5)

        if sugar % 3 == 0:
            pack_3 = sugar // 3
            return pack_5 + pack_3
    
    return -1

n = int(input())
print(min_cnt(n))


