# 진법 변환


import sys
input = sys.stdin.readline

n, b = input().split()
b = int(b)

# 파이썬 ㄷㄷㄷㄷ
# b진법 -> 10진법 변환
result = int(n, b)

# 결과 출력
print(result)