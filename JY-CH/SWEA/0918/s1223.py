# 계산기 2

def new_lst(lst):
    op = {
        '+': 1,
        '*': 2
    }

    lst1 = ''
    stack = []
    for idx in range(n):
        if lst[idx] in '0123456789':
            lst1 += lst[idx]

        else:
            if not stack:
                stack.append(lst[idx])
            else:
                if op[lst[idx]] > op[stack[-1]]:
                    stack.append(lst[idx])
                else:
                    while stack and op[lst[idx]] <= op[stack[-1]]:
                        a = stack.pop()
                        lst1 += a
                    stack.append(lst[idx])

    if stack:
        while stack:
            a = stack.pop()
            lst1 += a

    return lst1


def solve(new_lst):
    stack = []
    for idx in range(n):
        if new_lst[idx] in '0123456789':
            stack.append(int(new_lst[idx]))
        else:
            a = stack.pop()
            b = stack.pop()
            if new_lst[idx] == '+':
                stack.append(b + a)
            else:
                stack.append(b * a)

    return stack[-1]


for tc in range(1, 11):
    n = int(input())
    lst = input().strip()
    print(f'#{tc} {solve(new_lst(lst))}')