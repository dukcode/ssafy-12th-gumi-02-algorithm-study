# 계산기1

def made(lst):
    new_lst = ''
    stack = []
    for i in range(n):
        if lst[i] in '0123456789':
            new_lst += lst[i]
        else:
            if not stack:
                stack.append(lst[i])
            else:
                new_lst += stack.pop()
                stack.append(lst[i])
    while stack:
        new_lst += stack.pop()

    return new_lst

def finish(new_lst):
    stack = []
    for i in range(n):
        if new_lst[i] in '0123456789':
            stack.append(int(new_lst[i]))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1+num2)

    return stack.pop()


for tc in range(1, 11):
    n = int(input())
    lst = input().strip()
    lst1 = made(lst)
    result = finish(lst1)
    print(f'#{tc} {result}')