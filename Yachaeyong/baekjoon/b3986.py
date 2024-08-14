# 좋은 단어

N = int(input())

cnt = 0
for _ in range(N):
    
    stack = []
    words = input()
    for word in words:
        if not stack:
            stack.append(word)
        else: 
            if word == stack[-1]:
                stack.pop()
            else:
                stack.append(word)

    if len(stack) == 0:
        cnt += 1

print(cnt)