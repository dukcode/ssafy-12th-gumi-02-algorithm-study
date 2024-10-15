T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    switch = [list(map(int, input().split())) for _ in range(2)]
    result = 0

    for i in range(N):
        if switch[0][i] != switch[1][i]:
            for j in range(i, N):
                if switch[0][j] == 0:
                    switch[0][j] = 1
                elif switch[0][j] == 1:
                    switch[0][j] = 0
            result += 1

    print(f"#{tc} {result}")
