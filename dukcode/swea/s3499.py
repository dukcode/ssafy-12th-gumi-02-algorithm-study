t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    deck = input().split()
    half = (len(deck) + 1) // 2
    first_half = deck[:half]
    second_half = deck[half:]

    result = []
    for _ in range(len(second_half)):
        result.append(first_half.pop(0))
        result.append(second_half.pop(0))

    if len(first_half) != 0:
        result.append(first_half.pop(0))

    print(f"#{tc} {' '.join(result)}")
