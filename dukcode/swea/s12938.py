# subtree


def count_node(root):
    ret = 1

    for child in children[root]:
        ret += count_node(child)

    return ret


t = int(input())
for tc in range(1, t + 1):
    e, n = map(int, input().split())
    children = [[] for _ in range(e + 1)]

    arr = list(map(int, input().split()))
    for i in range(e):
        parent = arr[2 * i] - 1
        child = arr[2 * i + 1] - 1
        children[parent].append(child)

    print(f"#{tc} {count_node(n - 1)}")
