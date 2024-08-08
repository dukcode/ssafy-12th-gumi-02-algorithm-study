n = int(input())
calculation = input()
nums = [int(input()) for _ in range(n)]

stk = []
for i in calculation:
    if i.isalpha():
        stk.append(nums[ord(i) - ord("A")])
        continue

    b = stk.pop()
    a = stk.pop()

    if i == "+":
        stk.append(a + b)
    elif i == "-":
        stk.append(a - b)
    elif i == "*":
        stk.append(a * b)
    elif i == "/":
        stk.append(a / b)

print(f"{stk.pop():.2f}")
