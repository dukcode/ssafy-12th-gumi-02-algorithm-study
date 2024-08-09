import sys

sys.stdin = open("input.txt", "r")

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cnt = [0] * 200
    for _ in range(n):
        st, en = tuple(map(lambda x: (int(x) - 1) // 2, input().split()))
        if st > en:
            st, en = en, st

        for idx in range(st, en + 1):
            cnt[idx] = cnt[idx] + 1

    ans = max(cnt)
    print(f"#{tc} {ans}")
