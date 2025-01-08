# 주사위 3개

# 입력값 띄어서 정수형으로 받을거에요
a, b, c = map(int, input().split())

#
number_list = [a, b, c]



sorted(number_list)

# 같은 눈 3개
if a == b == c:
    print(10000 + (a * 1000))

# 같은 눈 2개
elif a == b != c:
    print(1000 + (a * 100))
elif a == c != b:
    print(1000 + (a * 100))
elif b == a != c:
    print(1000 + (b * 100))
elif b == c != a:
    print(1000 + (b * 100))
elif c == a != b:
    print(1000 + (c * 100))
elif c == b != a:
    print(1000 + (c * 100))

# 같은눈 없음.
# 생각해보니까 max 썼으면 됬는데 왜이랬을까

else:
    print((sorted(number_list)[2]) * 100)

# elif 노가다 했는데 뭔가 줄일 방법이 있지 않을까 생각중
