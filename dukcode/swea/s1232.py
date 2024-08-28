def calc(node):
    if isinstance(tree[node], int):
        return tree[node]

    op, left, right = tree[node]

    if op == "+":
        return calc(left) + calc(right)

    if op == "-":
        return calc(left) - calc(right)

    if op == "*":
        return calc(left) * calc(right)

    if op == "/":
        return calc(left) / calc(right)


T = 10
for tc in range(1, T + 1):
    n = int(input())

    tree = [None] * n
    for _ in range(n):
        tokens = list(input().split())

        node = int(tokens[0]) - 1

        if len(tokens) == 4:
            op = tokens[1]
            left_child = int(tokens[2]) - 1
            right_child = int(tokens[3]) - 1
            tree[node] = (op, left_child, right_child)
        else:
            num = int(tokens[1])
            tree[node] = num

    print(f"#{tc} {calc(0): .0f}")
