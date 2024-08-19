# 1234 비밀번호

for tc in range(1, 11):
    N, num = input().split()
    N = int(N)

    stack = []
    for n in num:
        if not stack:
            stack.append(n)
        else:
            if stack[-1] == n:
                stack.pop()
            else:
                stack.append(n)

    print(f'#{tc}', ''.join(stack))
