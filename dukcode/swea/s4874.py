t = int(input())


def calculate(calculation):
    stk = []
    for op in calculation:
        if op.isnumeric():
            stk.append(int(op))
            continue

        if op == ".":
            if len(stk) != 1:
                return "error"
            return stk[-1]

        if len(stk) < 2:
            return "error"

        b = stk.pop()
        a = stk.pop()
        if op == "+":
            stk.append(a + b)
        elif op == "-":
            stk.append(a - b)
        elif op == "*":
            stk.append(a * b)
        elif op == "/":
            stk.append(a // b)
        else:
            return "error"


for tc in range(1, t + 1):
    calculation = list(input().split())
    print(f"#{tc} {calculate(calculation)}")
