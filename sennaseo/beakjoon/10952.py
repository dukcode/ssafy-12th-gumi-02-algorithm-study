while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)
# while 문을 잘 몰라서 계속 for문과 if문을 돌렸다
# While True 다음의 식이 계속 True일때 계속된다는 뜻
# if 조건문을 완성하기까지 A, B = map(int, input().split())은 계속 돌아감.