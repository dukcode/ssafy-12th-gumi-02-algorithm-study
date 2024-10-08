# 숫자 카드
def find(data, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if data[mid] == target:
        return 1
    elif data[mid] > target:
        return find(data, target, start, mid - 1)
    else:
        return find(data, target, mid + 1, end)


N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
target = list(map(int, input().split()))

for t in target:
    print(find(cards, t, 0, N - 1), end=' ')
