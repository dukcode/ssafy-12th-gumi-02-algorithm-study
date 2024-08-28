T = int(input())
for tc in range(1, T+1):
    S = list(map(str, input()))
    cnt = 0
    for i in range(len(S) - 1):
        if S[i] == '(' and S[i+1] == ')':
            cnt += 1
        elif S[i] == '(' and S[i+1] == '|':
            cnt += 1
        elif S[i] == '|' and S[i+1] == ')':
            cnt += 1
    print(f'#{tc} {cnt}')