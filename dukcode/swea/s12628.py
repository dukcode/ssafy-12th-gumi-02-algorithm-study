t = int(input())


def solve(idx):
    if idx <= 1:
        return 1

    if cache[idx] != 0:
        return cache[idx]

    cache[idx] = solve(idx - 1) + solve(idx - 2) * 2
    return cache[idx]


for tc in range(1, t + 1):
    n = int(input()) // 10
    cache = [0] * (n + 1)
    print(f"#{tc} {solve(n)}")
