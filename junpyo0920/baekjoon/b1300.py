# if mid == 5
#   1   2   3  ->  3
#
#   2   4   6  ->  2
#
#   3   6   9  ->  1

# 3
# 7

#   1   2   3   4   5
#
#   2   4   6   8   10
#
#   3   6   9   12  15
#
#   4   8   12  16  20
#
#   5   10  15  20  25

def get_count_lte(num):
    count = 0
    for i in range(1, n + 1):
        count += min(n, num // i)
    return count


n = int(input())
k = int(input())

st = 1
en = n * n
ans = 0

while st <= en:
    half = (st + en) // 2
    idx_of_half = get_count_lte(half)

    if idx_of_half >= k:
        en = half - 1
        ans = half
        continue

    st = half + 1

print(ans)
