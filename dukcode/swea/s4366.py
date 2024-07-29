def solve():
    for i in range(1, len(binary)):
        binary[i] = (binary[i] + 1) % 2
        num = 0
        for n in binary:
            num = num * 2 + n

        ret = num
        changed_trit = []
        while num > 0:
            changed_trit.insert(0, num % 3)
            num //= 3

        if len(changed_trit) != len(trit):
            binary[i] = (binary[i] + 1) % 2
            continue
        cnt_changed = 0
        for idx in range(len(trit)):
            if changed_trit[idx] == trit[idx]:
                continue
            cnt_changed += 1

        if cnt_changed == 1:
            return ret

        binary[i] = (binary[i] + 1) % 2


t = int(input())
for tc in range(1, t + 1):
    binary = list(map(int, input()))
    trit = list(map(int, input()))

    print(f"#{tc} {solve()}")
