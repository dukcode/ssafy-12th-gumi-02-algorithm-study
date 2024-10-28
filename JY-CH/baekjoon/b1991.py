#트리 순회

import sys
input = sys.stdin.readline

# 전위 순회
def preorder(x):
    if x != '.':
        print(x, end='')
        preorder(tree[x][0])
        preorder(tree[x][1])

# 중위 순회
def inorder(x):
    if x != '.':
        inorder(tree[x][0])
        print(x, end='')
        inorder(tree[x][1])

# 후위 순회
def postorder(x):
    if x != '.':
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end='')



n = int(input())
tree = {}

for _ in range(n):
    mid, left, right = map(str, input().split())
    # 트리 구조니까 중간을 이용해 뻣어나가는 좌,우 체크
    tree[mid] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')

