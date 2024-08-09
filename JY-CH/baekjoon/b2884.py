# 알람 시계


# 정수형으로 입력 받을거에요
h, m = map(int, input().split())


#시간과 분의 범위 설정
0 <= h <= 23
0 <= m <= 59

#
if h > 0 and m < 45:
    print((h-1), (60 - (45-m)))
elif h == 0 and m < 45:
    print(23, (60-(45-m)))
else:
    print(h,(m-45))


