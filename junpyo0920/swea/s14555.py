for tc in range(int(input())):
    data = input()
    cnt = 0
    for i in range(len(data) - 1):
        now = data[i]
        next = data[i+1]
        if now == "(" and (next == ")" or next == "|"):
            cnt += 1
        elif now == "|" and next == ")":
            cnt += 1
    print(f"#{tc+1} {cnt}")