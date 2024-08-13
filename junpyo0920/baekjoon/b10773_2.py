K = int(input())
stack = [None] * K
top = -1

for _ in range(K):
    num = int(input())
    if not num:
        top -= 1
    else:
        top += 1
        stack[top] = num

ans = 0
for i in range(top+1):
    ans += stack[i]

print(ans)