expression = input()

i = 0
found_minus = False
ans = 0
while i < len(expression):
    if expression[i].isdecimal():
        num = ''
        for j in range(i, len(expression)):
            if not expression[j].isdecimal():
                num = int(num)
                i = j
                break

            num += expression[j]

            if j == len(expression) - 1:
                num = int(num)
                i = j + 1

        if found_minus:
            ans -= num
        else:
            ans += num
    else:
        if expression[i] == '-':
            found_minus = True
        i += 1

print(ans)