# 첫 번째 줄에 정수 K(앞으로 주어질 정수의 개수)가 주어진다. (1 ≤ K ≤ 100,000)
stack = [None] * 100000
top = -1

for _ in range(int(input())):
    n = int(input())
    if n:
        top += 1
        stack[top] = n
    else:
        # 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
        top -= 1

ans = 0
for i in range(top + 1):
    ans += stack[i]

print(ans)