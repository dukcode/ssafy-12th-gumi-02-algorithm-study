MX = 987_654_321

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    taken = [False] * n

    min_total = MX

    def solve(col_to_pick, total):
        global min_total

        if total >= min_total:
            return

        if col_to_pick == n:
            min_total = min(min_total, total)
            return

        for row in range(n):
            if taken[row]:
                continue

            taken[row] = True
            solve(col_to_pick + 1, total + board[row][col_to_pick])
            taken[row] = False

    solve(0, 0)
    print(f"#{tc} {min_total}")
