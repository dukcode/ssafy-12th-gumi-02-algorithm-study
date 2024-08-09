t = int(input())
for tc in range(1, t + 1):
    num = input()
    before = "0"
    cnt = 0
    for n in num:
        if before != n:
            cnt += 1
            before = n
    print(f"#{tc} {cnt}")
