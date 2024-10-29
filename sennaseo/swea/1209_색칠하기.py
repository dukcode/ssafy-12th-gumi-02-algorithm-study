T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [[0] * 10 for x in range(10)]
    cnt = 0
    for _ in range(N):

        r1, c1, r2, c2, color = map(int, input().split())

        if color == 1:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if graph[i][j] == 2:
                        cnt += 1
                    else:
                        graph[i][j] = color

        if color == 2:
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    if graph[i][j] == 1:
                        cnt += 1
                    else:
                        graph[i][j] = color

    print(f"#{tc} {cnt}")
