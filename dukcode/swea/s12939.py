t = int(input())


def create_tree(idx):
    global number

    if idx >= n:
        return

    create_tree(2 * idx + 1)
    tree[idx] = number
    number += 1
    create_tree(2 * idx + 2)


for tc in range(1, t + 1):
    n = int(input())

    tree = [0] * n
    number = 1
    create_tree(0)
    print(f"#{tc}", tree[0], tree[n // 2 - 1])
