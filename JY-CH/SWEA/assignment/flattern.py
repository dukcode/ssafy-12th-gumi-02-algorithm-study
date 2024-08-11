# flattern

def solve(lst, try_cnt):
    high = 0
    low = 100000000000
    for _ in range(try_cnt):
        high = max(lst)
        low = min(lst)

        high_idx = lst.index(high)
        low_idx = lst.index(low)

        lst[high_idx] -= 1
        lst[low_idx] += 1

    last_high = max(lst)
    last_low = min(lst)

    return last_high - last_low








for i in range(1, 11):
    tc = i
    try_cnt = int(input())
    lst = list(map(int, input().split()))
    result = solve(lst, try_cnt)
    print(f'#{tc} {result}')

