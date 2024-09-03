t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    capabilities = list(map(int, input().split()))

    weights.sort()
    weights.reverse()

    capabilities.sort()

    taken = [False] * n

    sum_weights = 0
    for capability in capabilities:
        for idx, weight in enumerate(weights):
            if not taken[idx] and weight <= capability:
                taken[idx] = True
                sum_weights += weight
                break

    print(f"#{tc} {sum_weights}")
