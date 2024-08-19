# 공과 잡초

T = int(input())
for tc in range(1, T + 1):

    S = input()

    cnt = 0
    for i in range(len(S)):
        if S[i] == '(':
            cnt += 1
        elif S[i] == ')':
            if 0 < i and S[i - 1] == '(':
                pass
            else:
                cnt += 1

    print(f'#{tc} {cnt}')
