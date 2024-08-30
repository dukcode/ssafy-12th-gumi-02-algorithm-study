def calc(idx):
    if idx >= n:
        return 0

    if tree[idx] != 0:
        return tree[idx]

    tree[idx] = calc(2 * idx + 1) + calc(2 * idx + 2)
    return tree[idx]


t = int(input())
for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    l -= 1

    tree = [0] * n
    for _ in range(m):
        idx, num = map(int, input().split())
        idx -= 1

        tree[idx] = num

    print(f"#{tc} {calc(l)}")
