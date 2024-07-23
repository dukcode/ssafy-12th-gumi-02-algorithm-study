# 사분면 고르기
x = int(input())
y = int(input())

x != 0
y != 0

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')