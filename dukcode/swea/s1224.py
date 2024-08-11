T = 10


def priority(op):
    if op == "*":
        return 1

    if op == "+":
        return 0

    return -1


def to_postfix(calculation):
    ret = []
    stk = []
    for op in calculation:
        if op.isdigit():
            ret.append(op)
            continue

        if op == "(":
            stk.append(op)
            continue

        if op == ")":
            while stk and stk[-1] != "(":
                ret.append(stk.pop())

            stk.pop()
            continue

        while stk and priority(op) <= priority(stk[-1]):
            ret.append(stk.pop())
        stk.append(op)

    while stk:
        ret.append(stk.pop())

    return ret


def calculate_postfix(postfix):

    stk = []
    for op in postfix:
        if op.isdigit():
            stk.append(int(op))
            continue

        b = stk.pop()
        a = stk.pop()

        if op == "+":
            stk.append(a + b)
        elif op == "*":
            stk.append(a * b)

    return stk[-1]


for tc in range(1, T + 1):
    n = int(input())
    calculation = input().strip()

    postfix = to_postfix(calculation)
    print(f"#{tc} {calculate_postfix(postfix)}")
