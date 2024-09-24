for tc in range(int(input())):
    max_s, data = input().split()
    max_s = int(max_s)
    counts = [0] * (max_s + 1)

    for i in range(max_s + 1):
        counts[i] = int(data[i])

    ans = 0
    for i in range(max_s + 1):
        if counts[i]:
            temp_standing = 0
            for j in range(i):
                temp_standing += counts[j]

            if temp_standing + ans < i:
                ans += i - temp_standing - ans

    print(f"Case #{tc+1}: {ans}")
