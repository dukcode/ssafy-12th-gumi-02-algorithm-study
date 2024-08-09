t = int(input())


def winner(st, en):
    if en - st == 0:
        return st

    half = (st + en) // 2
    first = winner(st, half)
    second = winner(half + 1, en)

    if arr[first] == arr[second]:
        return first

    if (arr[first] + arr[second]) % 2 == 1:
        if arr[first] > arr[second]:
            return first
        else:
            return second
    if arr[first] == 3 and arr[second] == 1:
        return second
    else:
        return first


for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"#{tc} {winner(0, n - 1) + 1}")
