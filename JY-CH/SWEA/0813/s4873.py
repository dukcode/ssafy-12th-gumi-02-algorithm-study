# 반복문자 지우기
# 스택

T = int(input())
for tc in range(1, T+1):
    word = input()

# 스택을 빈 리스트로
# 알파벳이 스택이 아니면
# 스택에 추가
    stack = []
    for apb in word:
        if not stack:
            stack.append(apb)
# 스택 끝자리와 비교
# 같으면 팝팝팝
# 아니면 추가!
        else:
            if stack[-1] == apb:
                stack.pop()
            else:
                stack.append(apb)

    print(f'#{tc} {len(stack)}')



