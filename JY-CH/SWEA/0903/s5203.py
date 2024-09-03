# 베이비진

N = 10
NUM_PLAYER = 2


def has_score(player, card):
    if cnt[player - 1][card] == 3:
        return True

    for last in range(card, card + 3):
        if last - 2 < 0 or last >= N:
            continue

        if 0 not in cnt[player - 1][last - 2:last + 1]:
            return True

    return False


def get_winner():
    for idx, c in enumerate(cards):
            p = idx % NUM_PLAYER + 1
            cnt[p - 1][c] += 1

            if has_score(p, c):
                return p

    return 0


def get_input():
    global cards
    cards = list(map(int, input().split()))


def init():
    global cnt
    cnt = [[0] * N for _ in range(NUM_PLAYER)]


cards = []
cnt = []
t = int(input())
for tc in range(1, t + 1):
    get_input()
    init()
    print(f'#{tc} {get_winner()}')
