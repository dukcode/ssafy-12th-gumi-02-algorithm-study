def to_binary_string(num):
    ret = ""

    i = 0.5
    while num > 0:
        if len(ret) > 13:
            return "overflow"

        if num - i >= 0:
            ret += "1"
            num -= i
        else:
            ret += "0"

        i /= 2

    return ret


t = int(input())
for tc in range(1, t + 1):
    number = float(input())
    print(f"#{tc} {to_binary_string(number)}")
