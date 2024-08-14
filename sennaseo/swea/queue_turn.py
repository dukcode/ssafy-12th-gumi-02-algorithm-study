def en_queue(data):
    global rear, front
    next = (rear + 1) % (N+1)
    if next == front:
        print("Queue_full")
    else:
        rear = next
        queue[rear] = data
 
def de_queue():
    global rear, front
    front = (front + 1) % (N+1)
    if rear == front:
        print("Queue_Empty")
    else:
        return queue[front]
 
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = [None] * (N+1)
    front, rear = 0, 0
    numbers = list(map(int, input().split()))
 
    for i in range(N):
        rear += 1
        queue[rear] = numbers[i]
 
    for x in range(M):
        en_queue(de_queue())
 
    print(f'#{tc} {de_queue()}')
