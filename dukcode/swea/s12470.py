t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [int(ch) for ch in input()]

    counts = [0] * 10

    max_cnt = -1
    max_num = -1
    for i in arr:
        counts[i] += 1

    max_cnt = -1
    for cnt in counts:
        if max_cnt < cnt:
            max_cnt = cnt

    max_num = -1
    for i in range(9, -1, -1):
        if counts[i] == max_cnt:
            max_num = i
            break

    print(f"#{tc} {max_num} {max_cnt}")
