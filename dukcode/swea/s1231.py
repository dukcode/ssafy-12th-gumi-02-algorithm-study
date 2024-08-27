T = 10


def inorder(root):
    if root >= n:
        return ""

    left = inorder(root * 2 + 1)
    right = inorder(root * 2 + 2)

    return left + tree[root] + right


for tc in range(1, T + 1):
    n = int(input())

    tree = [0] * n
    for _ in range(n):
        tokens = input().split()
        parent = int(tokens[0]) - 1
        word = tokens[1]

        tree[parent] = word

    print(f"#{tc} {inorder(0)}")
