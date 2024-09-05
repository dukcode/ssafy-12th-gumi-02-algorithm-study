# 동철이의 일 분배


def solve(person, prob):
    global max_prob

    if person == n:
        max_prob = max(max_prob, prob)
        return

    if prob <= max_prob:
        return

    for work in range(n):
        if taken[work]:
            continue

        taken[work] = True
        solve(person + 1, prob * arr[person][work])
        taken[work] = False


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(lambda i: int(i) / 100, input().split())) for _ in range(n)]

    taken = [False] * n
    max_prob = 0
    solve(0, 1.0)
    print(f"#{tc} {max_prob * 100:.6f}")
