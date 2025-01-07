# 괄호검사

T = int(input())
for tc in range(1, T+1):
    data = input()

    stack = []
    for sth in data:
        if sth == '(' or sth == '{':
            stack.append(sth)

    for i in range(len(data)):
        if stack == '(' and data[i] == ')' or stack == '{' and data[i] == '}':
            stack.pop()

    print(stack)






    # print(stack)
    # # print(f'{tc} {stack}')

