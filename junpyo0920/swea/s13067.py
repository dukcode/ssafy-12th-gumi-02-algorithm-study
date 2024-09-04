for tc in range(int(input())):
    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: x[1] or x[0])

    cnt = 1
    cur_end = data[0][1]
    for i in range(1, n):
        if data[i][0] >= cur_end:
            cnt += 1
            cur_end = data[i][1]

    print(f"#{tc+1} {cnt}")