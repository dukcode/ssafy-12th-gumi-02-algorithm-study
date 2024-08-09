import sys

sys.stdin = open("input.txt", "r")
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    moves = []
    for _ in range(n):
        st, en = tuple(map(lambda x: (int(x) - 1) // 2, input().split()))
        if st > en:
            st, en = en, st
        moves.append((st, en))

    moves.sort(key=lambda move: move[1])

    end_rooms = []
    for move in moves:
        st, en = move

        updated = False
        for idx in range(len(end_rooms) - 1, -1, -1):
            if end_rooms[idx] < st:
                end_rooms[idx] = en
                end_rooms.sort()
                updated = True
                break

        if not updated:
            end_rooms.append(en)

    print(f"#{tc} {len(end_rooms)}")
