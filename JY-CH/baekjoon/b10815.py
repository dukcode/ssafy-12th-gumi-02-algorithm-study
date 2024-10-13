# 숫자 카드


card = int(input())
card_num = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

def binary_search(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        half = (start + end) // 2

        if arr[half] == target:
            return 1

        if arr[half] > target:
            end = half
        else:
            start = half + 1

    return 0


for card in find:
    print(binary_search(card_num, card), end=' ')