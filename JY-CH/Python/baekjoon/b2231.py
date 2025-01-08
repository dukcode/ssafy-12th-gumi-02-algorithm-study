# 분해합

n = int(input())

for number in range(1, n + 1):
    div_num = list(map(int, str(number)))
    sum_num = sum(div_num) + number

    if sum_num == n:
        print(number)
        break
    else:
        continue
else:
    print(0)
