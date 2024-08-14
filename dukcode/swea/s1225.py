from collections import deque

T = 10
N = 5
for _ in range(1, T + 1):
    tc = int(input())
    q = deque(map(int, input().split()))

    to_sub = 0
    while True:
        over = False
        for to_sub in range(1, N + 1):
            num = q.popleft()
            num -= to_sub
            if num <= 0:
                q.append(0)
                over = True
                break

            q.append(num)

        if over:
            break

    print(f"#{tc}", *q)
