def inorder(node=1):
    if len(tree[node]) >= 2:
        inorder(int(tree[node][1]))

    print(tree[node][0], end="")

    if len(tree[node]) == 3:
        inorder(int(tree[node][2]))


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 2 for _ in range(N + 1)]
    for _ in range(N):
        data = input().split()
        tree[int(data[0])] = data[1:]
    print(f'#{tc}', end=" ")
    inorder()
    print()