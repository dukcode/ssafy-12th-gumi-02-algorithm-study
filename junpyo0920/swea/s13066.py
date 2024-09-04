for tc in range(int(input())):
    n, m = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)

    ans = 0
    for t in trucks:
        while weights:
            w = weights.pop(0)
            if t >= w:
                ans += w
                break

    print(f"#{tc+1} {ans}")
