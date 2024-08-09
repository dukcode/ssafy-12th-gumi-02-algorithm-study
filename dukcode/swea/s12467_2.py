t = int(input())


for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    chargers = tuple(map(int, input().split()))

    def solve():
        pos = 0
        cnt = 0
        while pos < n:
            moved = False
            for next in range(pos + k, pos, -1):
                if next >= n or next in chargers:
                    pos = next
                    moved = True
                    cnt += 1
                    break

            if not moved:
                return 0
        return cnt - 1

    ans = solve()
    print(f"#{tc} {ans}")
