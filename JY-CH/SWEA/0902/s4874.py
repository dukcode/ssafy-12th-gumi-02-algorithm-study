# forth


def solve(lst):
    stack = []
    for i in range(len(lst)):
        if lst[i] not in '*/+-.':
            stack.append(int(lst[i]))
        else:
            if lst[i] == '.':
                if len(stack) > 1 or not stack:
                    return 'error'
                else:
                    return stack[-1]

            if len(stack) < 2:
                return 'error'
            num2 = stack.pop()
            num1 = stack.pop()
            if lst[i] == '*':
                stack.append(num1*num2)
            elif lst[i] == '/':
                stack.append(num1//num2)
            elif lst[i] == '+':
                stack.append(num1+num2)
            elif lst[i] == '-':
                stack.append(num1-num2)




T = int(input())
for tc in range(1, T+1):
    lst = list(map(str, input().split()))
    result = solve(lst)

    print(f'#{tc} {result}')
