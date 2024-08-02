def count(st, en, target, cnt):
    half = (st + en) // 2

    if half == target:
        return cnt

    if target > half:
        return count(half, en, target, cnt + 1)

    return count(st, half, target, cnt + 1)


t = int(input())
for tc in range(1, t + 1):
    p, a, b = map(int, input().split())

    score_a = count(1, p, a, 0)
    score_b = count(1, p, b, 0)

    print(f"#{tc} ", end="")
    if score_a < score_b:
        print("A")
    elif score_a > score_b:
        print("B")
    else:
        print("0")
