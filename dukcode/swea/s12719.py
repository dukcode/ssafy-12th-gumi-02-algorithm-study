from collections import deque

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    candidate = deque(enumerate(map(int, input().split())))

    last_popped_index = -1
    cheese = deque()

    for _ in range(n):
        cheese.append(candidate.popleft())

    while cheese:
        c = cheese.popleft()

        if c[1] == 0:
            last_popped_index = c[0]

            if len(candidate) != 0:
                to_add = candidate.popleft()
                cheese.append((to_add[0], to_add[1] // 2))

            continue

        cheese.append((c[0], c[1] // 2))

    print(f"#{tc} {last_popped_index + 1}")
