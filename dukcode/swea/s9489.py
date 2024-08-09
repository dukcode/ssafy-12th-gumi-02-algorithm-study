import sys

sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t + 1):
    h, w = tuple(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(h)]

    ans = -1

    for row in board:
        tmp = "".join(map(str, row)).split("0")
        ans = max(ans, max(map(len, tmp)))

    for col in zip(*board):
        tmp = "".join(map(str, col)).split("0")
        ans = max(ans, max(map(len, tmp)))

    print(f"#{tc} {ans}")
