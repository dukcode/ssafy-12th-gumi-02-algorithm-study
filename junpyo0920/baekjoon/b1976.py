def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x == root_y:
        return

    if heights[root_x] < heights[root_y]:
        parents[root_x] = root_y
        heights[root_y] += 1
    else:
        parents[root_y] = root_x
        heights[root_x] += 1


n = int(input())
m = int(input())

heights = [0] * (n + 1)
parents = [x for x in range(n + 1)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union(i + 1, j + 1)

plans = list(map(int, input().split()))
is_connected = True

for i in range(1, len(plans)):
    prev_city = plans[i - 1]
    cur_city = plans[i]

    if parents[prev_city] == parents[cur_city]:
        continue

    is_connected = False
    break

print("YES" if is_connected else "NO")