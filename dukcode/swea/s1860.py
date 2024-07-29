t = int(input())
for tc in range(1, t + 1):
    n, m, k = tuple(map(int, input().split()))

    arrives = list(map(int, input().split()))
    arrives.sort()

    cnt = 0
    sec = 0
    possible = True
    for arrive in arrives:
        while True:
            if sec + m > arrive:
                break
            sec += m
            cnt += k

        if cnt == 0:
            possible = False
            break

        cnt -= 1

    print(f"#{tc} {'Possible' if possible else 'Impossible'}")
