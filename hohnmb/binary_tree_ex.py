# 5 4
# 1 2 1 3 3 4 3 5
n, m = map(int, input().split())

arr = list(map(int, input().split()))

tree = [[0] * (n + 1) for _ in range(2)]
# tree = [
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0]
# ]
# 왼쪽자식이 없으면 왼쪽에 넣고, 왼쪽자식이 있으면 오른쪽에 달기
for i in range(0, m * 2, 2):
    # print(arr[i], arr[i+1])
    if tree[0][arr[i]] == 0:
        tree[0][arr[i]] = arr[i + 1]
    else:
        tree[1][arr[i]] = arr[i + 1]

# 트리 순회하기
# 전위순회
# 중위순회
# 후위순회

def pre_order(v):
    if v == 0:  # 노드 아님
        return
    #현재 노드 먼저 처리하고
    #왼쪽 자식 > 오른쪽 자식
    print(v,end=' ')
    pre_order(tree[0][v])
    pre_order(tree[1][v])


def in_order(v):
    if v == 0:  # 노드 아님
        return
    #현재 노드 먼저 처리하고
    #왼쪽 자식 > 현재 > 오른쪽 자식
    in_order(tree[0][v])
    print(v, end=' ')
    in_order(tree[1][v])

def post_order(v):
    if v == 0:  # 노드 아님
        return
    #현재 노드 먼저 처리하고
    #왼쪽 자식 > 오른쪽 자식

    post_order(tree[0][v])
    post_order(tree[1][v])
    print(v, end=' ')

for row in tree:
    print(row)

pre_order(1)
print()
in_order(1)
print()
post_order(1)
print()







