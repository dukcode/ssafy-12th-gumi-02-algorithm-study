G = int(input())
P = int(input())

dock = [0] * (G + 1)


def find(x):
    if dock[x] != x:
        dock[x] = find(dock[x])
    return dock[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    if root_x < root_y:
        dock[root_y] = root_x
    else:
        dock[root_x] = root_y


for i in range(1, G + 1):
    dock[i] = i

cnt = 0
for _ in range(P):
    g = int(input())
    now_root = find(g)

    print(dock)
    if now_root == 0:
        break
    else:
        union(now_root, now_root-1)
        cnt += 1
print(cnt)
