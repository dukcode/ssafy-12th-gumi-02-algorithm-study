def traversal(node):
    global ans
    ans += 1
    if tree[node][0]:
        traversal(tree[node][0])
    if tree[node][1]:
        traversal(tree[node][1])


for tc in range(int(input())):
    e, n = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(e + 2)]
    for i in range(0, e * 2, 2):
        p_node, c_node = data[i], data[i + 1]
        if tree[p_node][0]:
            tree[p_node][1] = c_node
        else:
            tree[p_node][0] = c_node
    ans = 0
    traversal(n)
    print(f'#{tc + 1} {ans}')