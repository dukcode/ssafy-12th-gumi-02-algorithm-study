for tc in range(1, 10 + 1):
    num = int(input())
    heights = list(map(int, input().split()))

    count = [0] * 101
    for h in heights:
        count[h] += 1

    def get_min():
        for idx in range(len(count)):
            if count[idx] != 0:
                return idx

    def get_max():
        for idx in range(len(count) - 1, -1, -1):
            if count[idx] != 0:
                return idx

    for _ in range(num):
        min_h = get_min()
        max_h = get_max()

        if max_h - min_h == 1 or max_h - min_h == 0:
            break

        count[min_h] -= 1
        count[min_h + 1] += 1
        count[max_h] -= 1
        count[max_h - 1] += 1

    ans = get_max() - get_min()
    print(f"#{tc} {ans}")
