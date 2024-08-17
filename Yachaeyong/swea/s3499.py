T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = input().split()

    shuffle = []
    mid = N // 2
    if N % 2 == 0:
        f = cards[:mid]
        s = cards[mid:]
    else:
        f = cards[:mid + 1]
        s = cards[mid + 1:]

    for i in range(N):
        if i % 2 == 0:
            shuffle.append(f.pop(0))
        elif i % 2 == 1:
            shuffle.append(s.pop(0))

    print(f'#{tc}', *shuffle)
