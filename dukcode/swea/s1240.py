LEN_PER_NUM = 7
LEN_PASSCODE = LEN_PER_NUM * 8

# code -> num
DECODING_MAP = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}


def is_valid(decoded_nums):
    total = 0
    for idx, num in enumerate(decoded_nums):
        if idx % 2 == 0:
            total += num * 3
        else:
            total += num
    return total % 10 == 0


def decode(passcode):
    nums = []
    for idx in range(0, LEN_PASSCODE, LEN_PER_NUM):
        code = passcode[idx : idx + LEN_PER_NUM]
        num = DECODING_MAP[code]
        nums.append(num)

    return nums


def decode_from(y, x):
    passcode = arr[y][x : x + LEN_PASSCODE]
    return decode(passcode)


def find_start():
    for y in range(h):
        for x in reversed(range(w)):
            if arr[y][x] == "1":
                return (y, x - LEN_PASSCODE + 1)


def solve():
    nums = decode_from(*find_start())

    if is_valid(nums):
        return sum(nums)

    return 0


c = int(input())
for tc in range(1, c + 1):
    h, w = map(int, input().split())
    arr = [input() for _ in range(h)]

    ans = solve()
    print(f"#{tc} {ans}")
