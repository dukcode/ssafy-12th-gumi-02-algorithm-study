t = int(input())


for tc in range(1, t + 1):
    # n : 정류장의 총 갯수
    # k : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # m : 충전기의 갯수
    # arr : 충전기의 위치
    k, n, m = map(int, input().split())
    chargers = tuple(map(int, input().split()))

    def solve():
        pos = n
        cnt = 0
        while pos > 0:
            moved = False
            for next in range(pos - k, pos):
                if next <= 0 or next in chargers:
                    pos = next
                    cnt += 1
                    moved = True
                    break

            if not moved:
                return 0

        return cnt - 1

    ans = solve()
    print(f"#{tc} {ans}")
