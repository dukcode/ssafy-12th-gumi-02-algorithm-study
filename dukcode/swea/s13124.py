STOP = 0
RIGHT = 1
LEFT = -1


def get_dir(arr, m, target):
    if arr[m] < target:
        return RIGHT

    if arr[m] > target:
        return LEFT

    return STOP


def exists(arr: list, target: int) -> int:
    l = 0
    r = len(arr) - 1

    dir_before = STOP
    while l <= r:
        m = (l + r) // 2
        dir = get_dir(arr, m, target)
        if dir == STOP:
            return 1

        if dir == dir_before:
            return 0

        dir_before = dir

        if dir == RIGHT:
            l = m + 1

        if dir == LEFT:
            r = m - 1

    return 0


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    targets = list(map(int, input().split()))

    print(f"#{tc}", sum(list(map(lambda x: exists(arr, x), targets))))
