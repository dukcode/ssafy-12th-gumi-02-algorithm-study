def en_q(item):
    global rear
    next_r = (rear + 1) % (N + 1)
    if next_r != front:
        rear = next_r
        q[rear] = item


def de_q():
    global front
    if front != rear:
        front = (front + 1) % (N + 1)
        return q[front]


N, K = map(int, input().split())
q = [0] * (N + 1)
front = 0
rear = 0

for i in range(1, N + 1):
    rear = (rear + 1) % (N + 1)
    q[rear] = i

cnt = 1
ans = []
while front != rear:
    cur = de_q()
    if cnt % K:
        en_q(cur)
        cnt += 1
    else:
        ans.append(cur)
        cnt += 1

print(str(ans).replace('[', '<').replace(']', '>'))
