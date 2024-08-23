# 9012 괄호

T = int(input())
for _ in range(T):
    stack = []
    PS = input()

    for p in PS:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')