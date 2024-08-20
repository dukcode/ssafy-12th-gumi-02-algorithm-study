# https://www.acmicpc.net/problem/14888

def dfs(res, arr, cnt=1):
    if cnt == N:
        global max_num
        global min_num
        max_num = max(max_num, res)
        min_num = min(min_num, res)
        return

    if arr[0]:
        arr[0] -= 1
        dfs(res+nums[cnt], arr, cnt+1)
        arr[0] += 1
    if arr[1]:
        arr[1] -= 1
        dfs(res-nums[cnt], arr, cnt+1)
        arr[1] += 1
    if arr[2]:
        arr[2] -= 1
        dfs(res*nums[cnt], arr, cnt+1)
        arr[2] += 1
    if arr[3]:
        arr[3] -= 1
        if res < 0:
            dfs(-(-res//nums[cnt]), arr, cnt+1)
        else:
            dfs(res//nums[cnt], arr, cnt+1)
        arr[3] += 1


N = int(input())
nums = list(map(int, input().split()))
cnt_op = list(map(int, input().split()))

max_num = -1_000_000_000
min_num = 1_000_000_000

dfs(nums[0], cnt_op)
print(max_num)
print(min_num)
