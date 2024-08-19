w, h = map(int, input().split())
N = int(input())
columns = [0, w]
rows = [0, h]

for _ in range(N):
    data = list(map(int, input().split()))
    if data[0]:
        columns.append(data[1])
    else:
        rows.append(data[1])

columns.sort()
rows.sort()
ans = 0
for i in range(1, len(columns)):
    x = columns[i] - columns[i-1]
    for j in range(1, len(rows)):
        y = rows[j] - rows[j-1]
        ans = max(ans, x*y)
print(ans)
