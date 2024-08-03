DECODE = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9,
}

ENCODE = {
    0: "ZRO",
    1: "ONE",
    2: "TWO",
    3: "THR",
    4: "FOR",
    5: "FIV",
    6: "SIX",
    7: "SVN",
    8: "EGT",
    9: "NIN",
}


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


t = int(input())
for tc in range(1, t + 1):
    input()

    arr = input().split()
    arr = list(map(lambda x: DECODE[x], arr))
    selection_sort(arr)
    arr = list(map(lambda x: ENCODE[x], arr))

    print(f"#{tc}")
    print(*arr)
