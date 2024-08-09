import sys

sys.stdin = open("input.txt", "r")


def vertical_word_length(y, x):
    if y < 0 or y >= n:
        return 0

    if cache1[y][x] != -1:
        return cache1[y][x]

    if board[y][x] == 0:
        cache1[y][x] = 0
        return cache1[y][x]

    cache1[y][x] = 1 + vertical_word_length(y + 1, x)
    return cache1[y][x]


def horizontal_word_length(y, x):
    if x < 0 or x >= n:
        return 0

    if cache2[y][x] != -1:
        return cache2[y][x]

    if board[y][x] == 0:
        cache2[y][x] = 0
        return cache2[y][x]

    cache2[y][x] = 1 + horizontal_word_length(y, x + 1)
    return cache2[y][x]


def cnt_word_length(y, x, k):
    ret = 0
    if (y - 1 < 0 or board[y - 1][x] == 0) and vertical_word_length(y, x) == k:
        ret += 1
    if (x - 1 < 0 or board[y][x - 1] == 0) and horizontal_word_length(y, x) == k:
        ret += 1

    return ret


t = int(input())
for tc in range(1, t + 1):
    n, k = tuple(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    cache1 = [[-1] * n for _ in range(n)]
    cache2 = [[-1] * n for _ in range(n)]

    ans = 0
    for y in range(n):
        for x in range(n):
            ans += cnt_word_length(y, x, k)

    print(f"#{tc} {ans}")
