def getIdx(num, n):
    ret = 0
    for a in range(1, n + 1):
        b = num // a
        ret += min(b, n)
    return ret


def findIdx(n, k):
    st = 1
    en = min(10_000_000_001, n * n + 1)

    while st < en:
        half = (st + en) // 2
        idx = getIdx(half, n)
        if idx < k:
            st = half + 1
        else:
            en = half

    return st


n = int(input())
k = int(input())
print(findIdx(n, k))
