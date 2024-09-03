def is_runner(player):
    idx = player - 1
    for i in range(10 - 2):
        if cnt[idx][i] != 0 and cnt[idx][i + 1] != 0 and cnt[idx][i + 2]:
            return True

    return False


def is_triplet(player):
    idx = player - 1
    for i in range(10):
        if cnt[idx][i] >= 3:
            return True

    return False


t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input().split()))

    cnt = [[0] * 10 for _ in range(2)]

    ans = 0
    for idx, num in enumerate(arr):
        p = idx % 2 + 1
        cnt[p - 1][num] += 1
        if is_runner(p) or is_triplet(p):
            ans = p
            break

    print(f"#{tc} {ans}")
