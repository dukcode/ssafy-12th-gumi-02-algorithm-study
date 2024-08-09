MALE = 1
FEMAIL = 2


def print_switches(switches):
    for idx, switch in enumerate(switches):
        if idx != 0 and idx % 20 == 0:
            print()
        print(1 if switch else 0, end=" ")


def click(sex, num):
    if sex == MALE:
        for idx in range(len(switches)):
            if (idx + 1) % num == 0:
                switches[idx] = not switches[idx]
    else:
        idx = num - 1
        switches[idx] = not switches[idx]
        left = idx - 1
        right = idx + 1
        while True:
            if (left < 0 or right >= n) or switches[left] != switches[right]:
                break

            switches[left] = not switches[left]
            switches[right] = not switches[right]

            left -= 1
            right += 1


n = int(input())
switches = list(map(bool, map(int, input().split())))
m = int(input())
for _ in range(m):
    sex, num = tuple(map(int, input().split()))
    click(sex, num)

print_switches(switches)
