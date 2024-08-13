# 제로

K = int(input())

stack = []

for _ in range(K):
    num = int(input())

    if num != 0:
        stack.append(num)
    else:
        stack.pop()

total = 0
for s in stack:
    total += s

print(total)