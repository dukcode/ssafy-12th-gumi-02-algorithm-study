def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


g = int(input())
p = int(input())
parents = [x for x in range(g + 1)]

ans = 0

for _ in range(p):
    possible_gate = find(int(input()))
    if possible_gate == 0:
        break

    union(possible_gate, possible_gate - 1)
    ans += 1

print(ans)
