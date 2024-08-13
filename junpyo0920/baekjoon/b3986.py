cnt = 0
for _ in range(int(input())):
    word = input()
    if len(word) % 2:
        continue

    stack = [''] * 100000
    top = -1
    for ch in word:
        if top == -1 or ch != stack[top]:
            top += 1
            stack[top] = ch
        elif ch == stack[top]:
            stack[top] = ''
            top -= 1

    if top == -1:
        cnt += 1

print(cnt)
