# 두 수 비교하기

# a, b를 입력값으로 받을건데 정수형으로 받고 띄워서 받을거에요
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==') # 남은 조건은 하나밖에 없어 입력하지 않아도 된다