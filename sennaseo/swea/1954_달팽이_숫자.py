T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [x for x in range(1, N**2+1)]
    snail = [[0] * N for _ in range(N)]
    x = 0
    y = 0
    z = 0
    while arr[z] <= N**2:
        while x >= 0:
            while y >= 0:
                while 0 <= x < N:
                    while 0 <= y < N:
                        if snail[x][y] == 0:
                            snail[x][y] = arr[z]
                            z += 1
                            if y <= N-1:
                                y += 1
                            else:
                                break
                    x += 1
                if x >= N:
                    x -= 1
                y -= 1
            x -= 1
            if y < 0:
                continue
        if y < 0:
            y += 1
        if x < 0:
            x += 1
        if z >= N**2:
            break
    print(snail)