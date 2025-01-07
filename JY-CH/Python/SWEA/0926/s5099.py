# 피자 굽기
from collections import deque

for tc in range(int(input())):
    space, pizza = map(int, input().split())
    cheese = deque(enumerate(map(int, input().split())))
    queue = deque()

    for idx in range(space):
        queue.append(cheese.popleft())
    
    while len(queue) > 1:
        pizza_now = queue.popleft()

        if pizza_now[1] // 2 > 0:
            queue.append((pizza_now[0], pizza_now[1] // 2))
        else:
            if cheese:
                queue.append(cheese.popleft())
    
    print(f'#{tc + 1} {queue[0][0] + 1}')



