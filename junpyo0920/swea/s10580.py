for tc in range(int(input())):
    def is_contact(line1, line2):
        return ((line1[0] - line2[0]) < 0 and (line1[1] - line2[1]) > 0) or ((line1[0] - line2[0]) > 0 and (line1[1] - line2[1]) < 0)

    lines = [tuple(map(int, input().split())) for _ in range(int(input()))]
    ans = 0

    while len(lines) > 1:
        line1 = lines.pop()
        for line in lines:
           if is_contact(line1, line): ans += 1

    print(f'#{tc + 1} {ans}')
