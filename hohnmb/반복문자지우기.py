T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    for char in text:
        if stack and stack[-1] == char:
            stack.pop()
        else: 
            stack.append(char)
    result = len(stack)
 
    print(f'#{tc} {result}')