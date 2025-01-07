# itoa integer >> a
# 아스키 코드를 이용 숫자를 입력받아서
# 그 숫자에 해당하는 문자열을 반복하는 함수
# ex) 97 -> a / 65 -> A / 48 -> str(0)
# chr() : 아스키 코드 숫자에 해당하는 문자 반환
# ord() : 문자에 해당하는 아스키코드 반환
def itoa(arg):       # str()
    # 숫자를 하나씩 잘라서 그 숫자에 해당하는 문자열로 만들어서
    # 423 > 4,2,3
    # 4 >> '4' , 2 >> '2', 3 >> '3'
    # '423'
    # 1. 숫자를 각자리수 대로 자르기
    # 1-1 인자로 받은 숫자를 10으로 나누어서 몫에 저장
    # 1-2 나머지를 문자열로 바꾸어서 저장
    # 1-3 1-1, 1-2의 과정을 몫이 0이 될 때 까지 반복
    num = arg
    result = '' # 결과를 저장하기 위한 변수
    while num > 0:
        a = num // 10
        b = num % 10
        result = chr(ord('0') + b) + result
        num = a
    return result


arr = []
arr.append(itoa(123))
arr.append(itoa(456))
print(arr)


def atoi(arg):
    # 문자열도 하나 하나 끊어서 아스키 코드표 참조
    # 해서 숫자로 변경
    # 문자열을 하나씩 끊어서 숫자로 바꾸어서 저장할건데
    # 새로운 숫자를 얻을때마다 기존 숫자에는 10곱해서 더해주기
    result = 0
    for i in range(len(arg)):
        # ord(arg[i]) - ord('0') : 문자에 대한 숫자 얻기
        result * 10
        result += ord(arg[i]) - ord('0')
    return result

print(atoi('542') + atoi('58'))