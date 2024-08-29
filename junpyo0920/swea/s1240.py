key_data = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9
}

for tc in range(int(input())):
    h, w = map(int, input().split())
    key = [[] for _ in range(8)]

    for _ in range(h):
        data = input()
        if int(data):
            temp_key = [x for x in data.rstrip("0")]
            while len(temp_key) != 56:
                temp_key.pop(0)
            for i in range(8):
                key[i] = "".join(temp_key[i * 7:i * 7 + 7])

    for i, k in enumerate(key):
        key[i] = key_data.get(k)

    odd = 0
    even = 0

    for i in range(8):
        odd += key[i] if (i + 1) % 2 else 0
        even += key[i] if not (i + 1) % 2 else 0

    print(f"#{tc + 1}", end=" ")

    if (odd * 3 + even) % 10 == 0:
        print(odd + even)
    else:
        print(0)