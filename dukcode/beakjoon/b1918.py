calculation = input()


def priority(op):
    if op == "*" or op == "/":
        return 1

    if op == "+" or op == "-":
        return 0

    return -1


stk = []
ans = []
for i in calculation:
    if i.isalpha():
        ans.append(i)
        continue

    if i == "(":
        stk.append(i)
        continue

    if i == ")":
        while stk and (j := stk.pop()) != "(":
            ans.append(j)
        continue

    while stk and stk[-1] != "(" and priority(stk[-1]) >= priority(i):
        ans.append(stk.pop())
    stk.append(i)

while stk:
    ans.append(stk.pop())

print(*ans, sep="")
