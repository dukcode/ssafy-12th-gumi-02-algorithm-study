T = int(input())
for tc in range(1, T + 1):
    array = input()
    stack = []
    ans = 0
    for i in range(len(array)):
        if array[i] == "(":
            if i + 1 < len(array) and array[i + 1] == ")":
                ans += len(stack)
            else:
                stack.append("(")
        elif array[i] == ")":
            if i - 1 >= 0 and array[i - 1] == "(":
                continue
            stack.pop()
            ans += 1

    print(f"#{tc} {ans}")

# 왼쪽 끝 '('을 stack에 append한다. 오른쪽 끝 ')'을 만나면 1개의 쇠막대기가 되므로 한 쌍이 된 왼쪽끝 '('을 pop 해준다
# 레이저로 잘리면 잘린 단면이 새로운 오른쪽 끝이 된다 -> stack 안의 왼쪽 끝 수 만큼 쇠막대기 수에 더해주면 됨.
# 또한 기존 왼쪽 끝 수 만큼 새로운 왼쪽 끝 쪽이 생긴다 -> stack 안의 왼쪽 끝 수를 그대로 두면 됨.
