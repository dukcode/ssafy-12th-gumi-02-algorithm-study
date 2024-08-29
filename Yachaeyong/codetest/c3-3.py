# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4
N, M = map(int, input().split())

card = [list(map(int, input().split())) for _ in range(N)]

ans = []
for row in card:
    min_v = 10001
    for r in row:
        if min_v > r:
            min_v = r
    ans.append(min_v)

max_v = 0
for a in ans:
    if max_v < a:
        max_v = a
print(max_v)