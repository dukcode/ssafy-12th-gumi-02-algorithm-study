from collections import deque


def bfs(start):
    queue = deque([(start, 0)])
    nums = {start}
    while queue:
        cur_num, cnt = queue.popleft()

        if cur_num == m:
            return cnt

        for next in (cur_num + 1, cur_num - 1, cur_num * 2, cur_num - 10):
            if 0 < next <= 1000000 and next not in nums:
                queue.append((next, cnt + 1))
                nums.add(next)
    return -1


for tc in range(int(input())):
    n, m = map(int, input().split())
    print(f"#{tc+1} {bfs(n)}")
