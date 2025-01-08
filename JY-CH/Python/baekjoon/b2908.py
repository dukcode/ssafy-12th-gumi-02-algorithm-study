# 상수


# 내? 준표? 풀이.

number1, number2 = input().split()
number1 = list(number1)
number1 = int(''.join(list(reversed(number1))))

number2 = list(number2)
number2 = int(''.join(list(reversed(number2))))

if number1 > number2:
    print(number1)
else :
    print(number2)


# 일반적으로는 뒤집혀지지 않아서
# 리스트로 바꾸고, 뒤집은다음 붙여야되는데
# 못 붙이고 있는걸 준표가 알랴줌
# 과목평가때 안나올줄 알고 공부 안했다가 봉변 당하는중. 


# 찾아본 풀이

# num1, num2 = input().split()
# num1 = int(num1[::-1])  # [::-1] : 역순
# num2 = int(num2[::-1])

# if num1 > num2:
#     print(num1)
# else :
#     print(num2)

# 줄도 짧고 깔끔함.
# 슬라이싱을 생각했더라면 이렇게 풀었을지도..