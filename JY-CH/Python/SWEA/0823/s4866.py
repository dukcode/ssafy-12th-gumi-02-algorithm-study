# 괄호검사

T = int(input())
for tc in range(1, T+1):
    data = input()

    stack = []
    for sth in data:
        if sth == '(' or sth == '{':
            stack.append(sth)

        elif sth == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break

        elif sth == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break

    else:
        result = 1

    if stack or result == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')

