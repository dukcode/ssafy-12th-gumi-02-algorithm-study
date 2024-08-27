def inorder(node=1):
    global num

    if node * 2 <= N:
        inorder(node * 2)

    arr[node] = num
    num += 1

    if node * 2 + 1 <= N:
        inorder(node * 2 + 1)


for tc in range(int(input())):
    N = int(input())
    arr = [0] * (N + 1)
    num = 1
    inorder()
    print(f'#{tc + 1} {arr[1]} {arr[N // 2]}')