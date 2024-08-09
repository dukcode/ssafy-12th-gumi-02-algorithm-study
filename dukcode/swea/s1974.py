import sys

sys.stdin = open("input.txt", "r")


t = int(input())
for tc in range(1, t + 1):
    board = [list(map(int, input().split())) for _ in range(9)]

    is_complete = True

    for row in board:
        if len(set(row)) != 9:
            is_complete = False
            break

    if not is_complete:
        print(f"#{tc} 0")
        continue

    for col in zip(*board):
        if (len(set(col))) != 9:
            is_complete = False
            break

    if not is_complete:
        print(f"#{tc} 0")
        continue

    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            num_set = set()
            for dy in range(0, 3):
                for dx in range(0, 3):
                    num_set.add(board[y + dy][x + dx])
            if len(num_set) != 9:
                is_complete = False
                break
        if not is_complete:
            break

    if not is_complete:
        print(f"#{tc} 0")
        continue

    print(f"#{tc} 1")
