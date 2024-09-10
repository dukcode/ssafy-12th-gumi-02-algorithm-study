def solve(total, idx):
    if idx == n:
        global min_res, max_res
        min_res = min(min_res, total)
        max_res = max(max_res, total)
        return

    for i in range(4):
        if not op_cnt[i]:
            continue

        if i == 0:
            op_cnt[i] -= 1
            solve(total + nums[idx], idx + 1)
            op_cnt[i] += 1

        if i == 1:
            op_cnt[i] -= 1
            solve(total - nums[idx], idx + 1)
            op_cnt[i] += 1

        if i == 2:
            op_cnt[i] -= 1
            solve(total * nums[idx], idx + 1)
            op_cnt[i] += 1

        if i == 3:
            op_cnt[i] -= 1
            if total < 0 or nums[idx] < 0:
                solve(-(abs(total) // abs(nums[idx])), idx + 1)
            else:
                solve(total // nums[idx], idx + 1)
            op_cnt[i] += 1


for tc in range(int(input())):
    n = int(input())
    op_cnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    min_res = 0xFFFFFFFF
    max_res = -0xFFFFFFFF
    solve(nums[0], 1)
    print(f"#{tc+1} {max_res - min_res}")