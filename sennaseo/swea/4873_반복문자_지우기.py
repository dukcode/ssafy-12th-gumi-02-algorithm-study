def Duplicate_test(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    return len(stack)


T = int(input())
for tc in range(1, T + 1):
    s = input()
    print(f"#{tc} {Duplicate_test(s)}")
