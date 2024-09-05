# 전기버스2 - 그리디 풀이


def solve():
    cnt = 0
    pos = 0
    battery = arr[0]

    while True:
        max_potential = 0
        best_move = 0
        for move in range(1, battery + 1):

            next_pos = pos + move

            if next_pos >= n:
                return cnt

            potential = pos + move + arr[next_pos]

            if potential > max_potential:
                max_potential = potential
                best_move = move

        cnt += 1
        pos = pos + best_move
        battery = arr[pos]


t = int(input())
for tc in range(1, t + 1):
    n, *arr = list(map(int, input().split()))
    n -= 1
    print(f"#{tc} {solve()}")
