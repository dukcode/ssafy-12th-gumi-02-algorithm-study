code = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())
for tc in range(1, T + 1):
    test, N = input().split()
    num = int(N)
    words = list(input().split())

    counts = [0] * 10
    result = [0] * num
    for word in words:
        counts[code[word]] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    for i in range(num - 1, -1, -1):
        counts[code[words[i]]] -= 1
        result[counts[code[words[i]]]] = words[i]

    # for i in range(num-1):
    #     min_idx = i
    #     for j in range(i+1, num):
    #         if code[words[min_idx]] > code[words[j]]:
    #             min_idx = j
    #     words[i], words[min_idx] = words[min_idx], words[i]

    print(test)
    print(*result)
