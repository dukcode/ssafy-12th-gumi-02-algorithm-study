#  균형잡힌 세상
while True:
    data = input()
    stack = []

    if data == '.':
        break

    for d in data:
        if d in '([':
            stack.append(d)
        elif d == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(d)
                break
        elif d == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(d)
                break

    if not stack:
        print('yes')
    else:
        print('no')

