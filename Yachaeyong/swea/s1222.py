def change(data):  # 중위 표기식을 후위 표기식으로 바꾸기
    stack = []
    exp = ''
    # 숫자이면 exp에 넣고 +는 스택에 넣기
    for i in range(N):
        if data[i] in '0123456789':
            exp += data[i]
        else:
            if not stack:  # 스택 비어있으면 + 추가
                stack.append(data[i])
            else:  # 안 비었으면 원래 있던 + 빼서 exp에 붙이고 다시 + 넣기
                exp += stack.pop()
                stack.append(data[i])
    while stack:
        exp += stack.pop()  # 마지막에 남은 + 다 붙이기
    return exp


def calculate(exp):  # 후위 표기식을 계산하기
    stack = []
    # 스택에 다 넣고 연산자 만나면 pop 한 결과 더해서 다시 넣기
    for i in range(N):
        if exp[i] in '0123456789':
            stack.append(int(exp[i]))
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)

    return stack[-1]


for tc in range(1, 11):
    N = int(input())
    data = input().strip()

    result = calculate(change(data))
    print(f'#{tc} {result}')
