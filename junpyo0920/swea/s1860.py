def time_flies():
    global cnt
    for sec in range(guests[-1] + 1):
        if sec != 0 and sec % M == 0:
            cnt += K
        while guests and sec == guests[0]:
            cnt -= 1
            if cnt < 0:
                print(f'#{tc + 1} Impossible')
                return
            guests.pop(0)
    print(f'#{tc + 1} Possible')


for tc in range(int(input())):
    N, M, K = map(int, input().split())
    guests = sorted(list(map(int, input().split())))
    if guests[0] < M:
        print(f'#{tc + 1} Impossible')
        continue

    cnt = 0
    time_flies()
