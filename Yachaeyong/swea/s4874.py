def forth(exp):
    stack = []
    ans = 0

    for e in exp:
        # 연산자인 경우
        if e in '+-*/.':
            # . 만나면 스택에서 숫자 꺼내 출력
            if e == '.':
                if len(stack) != 1:
                    return 'error'
                else:
                    return stack.pop()
            elif len(stack) < 2:
                return 'error'
            # . 아닌 다른 연산자 만나면
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if e == '+':
                    stack.append(num1 + num2)
                elif e == '-':
                    stack.append(num1 - num2)
                elif e == '*':
                    stack.append(num1 * num2)
                elif e == '/':
                    stack.append(num1 // num2)
        else:  # 숫자인 경우
            stack.append(int(e))

    if len(stack) != 1:
        return 'error'

    return ans


T = int(input())

for tc in range(1, T + 1):
    exp = input().strip().split()

    result = forth(exp)

    print(f'#{tc} {result}')
