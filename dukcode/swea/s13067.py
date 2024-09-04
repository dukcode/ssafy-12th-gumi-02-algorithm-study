t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    times = []
    for _ in range(n):
        s, e = map(int, input().split())
        times.append((s, e))

    times.sort(key=lambda t: (t[1], t[0]))

    cnt = 0
    last_end = 0
    for time in times:
        if last_end <= time[0]:
            cnt += 1
            last_end = time[1]

    print(f"#{tc} {cnt}")
