# 윤년


# 입력값을 정수형으로 받을거에요
year = int(input())


# 요구사항을 잘 읽어야 되는 문제.

# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다

# ((4의 배수) 이면서(=and) (100의 배수가 아닐떄)) / 또는(=or) (400의 배수)
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('1')
# elif year % 400 == 0:
#     print('1')
else:
    print('0')

# elif 쓰고 돌릴려다 왠지 줄일 수 있을거 같아서 해봤는데 진짜됬음.

# **한국말 잘 읽기**

# 조건을 한줄에 다중으로 걸고 싶다면 요구사항을 잘 확인하고 ()를 잘 칠것.