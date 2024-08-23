def dfs(count, num):
    global best_num
    if count == change:
        best_num = max(best_num, "".join(num))
        return

    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            current_num = "".join(num)

            if (current_num, count) not in visited:
                visited.add((current_num, count))
                dfs(count + 1, num)

            num[i], num[j] = num[j], num[i]


T = int(input())
for t in range(1, T + 1):
    num, change = input().split()
    num = list(num)
    change = int(change)

    best_num = "".join(num)
    visited = set()
    dfs(0, num)
    print(f"#{t} {best_num}")
