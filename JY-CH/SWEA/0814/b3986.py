# 좋은 단어

N = int(input())
cnt = 0
for _ in range(N):
    word = input()

    stack = []
    for i in word:
        # 불리언이다.
        # if not stack = stack이 비었다면을 의미한다.
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)

    if not stack:
        cnt += 1

print(cnt)