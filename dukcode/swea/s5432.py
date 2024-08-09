t = int(input())
for tc in range(1, t + 1):
    line = input()
    ans = 0
    cnt = 0
    for idx in range(len(line)):
        if line[idx] == "(":
            cnt += 1
            continue

        if line[idx] == ")" and line[idx - 1] == "(":
            cnt -= 1
            ans += cnt
            continue

        if line[idx] == ")":
            cnt -= 1
            ans += 1

    print(f"#{tc} {ans + cnt}")
