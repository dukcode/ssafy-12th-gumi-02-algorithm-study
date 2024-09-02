# 최소합


# 함수
# 스타트y, 스타트x
def solve(sy, sx, sum_v):
    global min_v
    # 최소합을 넘의면 의미가 없음.
    if sum_v >= min_v:
        return

    # 이동한계 초과시
    if sy >= N or sx >= N:
        return

    # 목적지 도착시 추가수행 의미 x
    if (sy, sx) == (N-1, N-1):
        result = sum_v + data[sy][sx]
        if result < min_v:
            min_v = result
        return

    # 아니라면?
    # 두가지 조건에 맞춰 재귀
    solve(sy, sx + 1, sum_v + data[sy][sx])
    solve(sy + 1, sx, sum_v + data[sy][sx])










T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    min_v = 9999999
    solve(0, 0, 0)
    print(f'#{tc} {min_v}')