# 암기왕
def check(data, target, start, end):
    s, e = start, end
    while s <= e:
        mid = (s + e) // 2

        if data[mid] == target:
            return 1
        elif data[mid] > target:
            e = mid - 1
        else:
            s = mid + 1

    return 0


T = int(input())
for _ in range(T):
    N = int(input())
    note = list(map(int, input().split()))
    note.sort()
    M = int(input())
    target = list(map(int, input().split()))

    for t in target:
        print(check(note, t, 0, N - 1))