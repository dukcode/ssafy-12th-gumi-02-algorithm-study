for tc in range(int(input())):
    ans = 0
    layout = input()
    cnt = 0
    for idx, char in enumerate(layout):
        if char == '(':
            cnt += 1
        else:
            if layout[idx - 1] == '(':
                cnt -= 1
                ans += cnt
            else:
                cnt -= 1
                ans += 1
    print(f'#{tc + 1} {ans}')