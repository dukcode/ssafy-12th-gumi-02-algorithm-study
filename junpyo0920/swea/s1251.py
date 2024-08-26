def prim(start):
    visited = [start]
    distance = 0

    for _ in range(n-1):
        min_dist, next_node = (1000000 ** 2) * 2, -1
        for node in visited:
            for i in range(n):
                if i not in visited and data[node][i] < min_dist:
                    min_dist = data[node][i]
                    next_node = i
        visited.append(next_node)
        distance += min_dist

    return distance


for tc in range(int(input())):
    n = int(input())
    x_axis = list(map(int, input().split()))
    y_axis = list(map(int, input().split()))
    e = float(input())
    data = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            data[i][j] = (x_axis[i] - x_axis[j])**2 + (y_axis[i] - y_axis[j])**2

    ans = (1000000 ** 2) * 2 * (n-1)
    print(f'#{tc+1} {round(prim(0) * e)}')