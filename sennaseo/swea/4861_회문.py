T = int(input())


def solve(data):
    for i in range(N):
        for j in range(N - M + 1):
            is_find = True
            for plus in range(M // 2):
                if data[i][j + plus] != data[i][j + M - 1 - plus]:
                    is_find = False
                    break

            if is_find:
                return data[i][j : j + M]
    return None


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    result = solve(data)
    if not result:
        result = solve(list(map("".join, zip(*data))))
    print(f"#{tc} {result}")
