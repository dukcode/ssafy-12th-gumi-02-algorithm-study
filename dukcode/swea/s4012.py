MX = 987_654_321

t = int(input())


def calc():
    score1 = 0
    score2 = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if taken[i] and taken[j]:
                score1 += arr[i][j] + arr[j][i]
            if not taken[i] and not taken[j]:
                score2 += arr[i][j] + arr[j][i]

    return abs(score1 - score2)


def solve(last_idx, cnt):

    if cnt == n // 2:
        return calc()

    ret = MX
    for next_idx in range(last_idx + 1, n):
        taken[next_idx] = True
        ret = min(ret, solve(next_idx, cnt + 1))
        taken[next_idx] = False

    return ret


for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    taken = [False] * n
    print(f"#{tc} {solve(-1, 0)}")
