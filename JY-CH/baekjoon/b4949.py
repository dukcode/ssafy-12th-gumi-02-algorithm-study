# 균형잡힌 세상

import sys
input = sys.stdin.readline


while True:
    # input = sys.stdin.readline은 그냥 받을시 개행문자를 제거해줘야함.
    # strip()을 사용한 이유
    data = list(input().strip('\n'))
    # print(data)
    # 온점일때 while문 종료
    if data[0] == '.':
        break

    stack = []
    # 조건 다 통과하면 yes 아니면 no
    result = 'yes'

    for word in data:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if len(stack) == 0 or stack[-1] != '(':
                result = 'no'
                break
            stack.pop()

        elif word == ']':
            if len(stack) == 0 or stack[-1] != '[':
                result = 'no'
                break
            stack.pop()

    if len(stack) > 0:
        result = 'no'

    print(result)
            