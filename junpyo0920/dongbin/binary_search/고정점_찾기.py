# 5
# -15 -6 1 3 7
# 7
# -15 -4 2 8 9 13 15
# 7
# -15 -4 3 8 9 13 15
# -10 -5 0 5 10

def solve(s, e):
    while s <= e:
        mid = (s + e) // 2

        if nums[mid] == mid:
            print(mid)
            return

        if nums[mid] < 0 or nums[mid] < mid:
            s = mid + 1
            continue

        e = mid - 1
        continue

    print(-1)


n = int(input())
nums = list(map(int, input().split()))
solve(0, n)
