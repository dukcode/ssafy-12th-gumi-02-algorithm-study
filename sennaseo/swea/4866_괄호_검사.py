T = int(input())
for tc in range(1, T+1):
    array = input()

    stack = []
    result = 1

    for arr in array:
        if arr == '(' or arr == '{':
            stack.append(arr)

        elif arr == ')':
            if not stack or stack.pop() != '(':
                result = 0
                break
        elif arr == '}':
            if not stack or stack.pop() != '{':
                result = 0
                break
    if stack:
        result = 0

    print(f'#{tc} {result}')