# O(100_000_000)
t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    lines = []

    for _ in range(n):
        a, b = tuple(map(int, input().split()))
        lines.append((a, b))

    ans = 0
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            if (lines[i][0] - lines[j][0]) * (lines[i][1] - lines[j][1]) < 0:
                ans += 1

    print(f"#{tc} {ans}")
