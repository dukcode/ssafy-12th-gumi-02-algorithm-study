# 인풋 메소드는 마지막 줄일때 EOFERROR를발생시키는데, 에러가 발생하면 except문으로 받아서 반복문을 탈출함.
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except :
        break