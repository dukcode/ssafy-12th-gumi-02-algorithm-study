for tc in range(1, 11):
    N, t = input().split()
    stack = []
    for ch in t:
        if not stack:
            stack.append(ch)
        elif ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    print(f'#{tc} {"".join(stack)}')