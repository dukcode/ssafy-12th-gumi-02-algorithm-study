# 중위 순회

def inorder(x):
    # 조건, x를 넣고 중위순회를 시작하되, n을 넘을 수 는 없다.
    # 좌 중 우
    if x <= n:
        # 좌, 짝수 노드
        inorder(x * 2)
        print(tree[x], end='')
        # 우, 홀수 노드
        inorder((x * 2) + 1)


t = 10
for tc in range(1, t+1):
    n = int(input())
    tree = {}
    for _ in range(n):
        # 전날에 한거랑 달리 .을 안찍고 공백을 줘서 그냥 다 받아야됨
        data = input().split()
        # 입력값 첫번째 순대로 key값 받아서 저장
        # data[1] => 문자
        tree[int(data[0])] = data[1]


    print(f'#{tc}', end=' ')
    inorder(1)
    print()

