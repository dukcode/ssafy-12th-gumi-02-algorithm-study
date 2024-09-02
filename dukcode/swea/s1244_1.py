# 최대 상금
def solve(nums, cnt):
    score = int("".join(map(str, nums)))
    if cnt == 0:
        return score

    if cache.get((score, cnt), -1) != -1:
        return cache.get((score, cnt))

    ret = 0
    for first in range(len(nums)):
        for second in range(first + 1, len(nums)):
            nums[first], nums[second] = nums[second], nums[first]
            ret = max(ret, solve(nums, cnt - 1))
            nums[first], nums[second] = nums[second], nums[first]

    cache[(score, cnt)] = ret
    return ret


t = int(input())
for tc in range(1, t + 1):
    cache = {}

    tokens = input().split()
    nums = list(map(int, tokens[0]))
    cnt = int(tokens[1])
    print(f"#{tc} {solve(nums, cnt)}")
