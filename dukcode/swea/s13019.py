def to_binary_string(hex):
    ret = ""
    for num in hex:
        binary_str = ""
        if num in "ABCEDF":
            num = ord(num) - ord("A") + 10
        else:
            num = int(num)

        for _ in range(4):
            binary_str += str(num % 2)
            num //= 2

        ret += binary_str[::-1]

    return ret


t = int(input())

for tc in range(1, t + 1):
    n, hex_str = input().split()
    n = int(n)
    print(f"#{tc} {to_binary_string(hex_str)}")
