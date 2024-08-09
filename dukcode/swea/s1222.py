def priority(op):
    if op == "+" or op == "-":
        return 0

    if op == "*" or op == "/":
        return 1

    return -1


def to_postfix(calculation):
    ret = []
    stk = []
    for ch in calculation:
        if ch.isnumeric():
            ret.append(int(ch))
            continue

        while stk:
            ret.append(stk.pop())

        stk.append(ch)

    while stk:
        ret.append(stk.pop())

    return ret


def calculate(postfix):
    stk = []
    for i in postfix:
        if i == "+":
            a = stk.pop()
            b = stk.pop()
            stk.append(a + b)
            continue

        stk.append(i)

    return stk[-1]


T = 10
for tc in range(1, T + 1):
    n = int(input())
    calculation = input().strip()

    postfix = to_postfix(calculation)
    print(f"#{tc} {calculate(postfix)}")
