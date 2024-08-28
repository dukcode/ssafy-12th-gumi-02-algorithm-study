t = int(input())


def insert(num):
    global last, heap
    last += 1

    heap[last] = num

    idx = last
    parent_idx = idx // 2
    while parent_idx >= 1 and heap[parent_idx] > heap[idx]:
        heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
        idx = parent_idx
        parent_idx = idx // 2


for tc in range(1, t + 1):
    n = int(input())

    heap = [0] * (n + 1)
    last = 0
    arr = list(map(int, input().split()))

    for num in arr:
        insert(num)

    ans = 0
    node = last // 2
    while node >= 1:
        ans += heap[node]
        node //= 2

    print(f"#{tc} {ans}")
