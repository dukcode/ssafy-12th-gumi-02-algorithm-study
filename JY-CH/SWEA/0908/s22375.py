# 스위치 조작
OFF = 0
ON = 1


def press(swtch):
    for idx in range(swtch, switch_num):
        if before[idx] == OFF:
            before[idx] = ON
        else:  # ON
            before[idx] = OFF


def match(swtch, before, after):
    return before[swtch] == after[swtch]


for tc in range(int(input())):
    switch_num = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))

    cnt = 0
    for switch in range(switch_num):
        if not match(switch, before, after):
            cnt += 1
            press(switch)

    print(f'#{tc + 1} {cnt}')
