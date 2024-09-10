from collections import deque


def bfs(start):
    q = deque([(start, 0)])
    checked = [0] * 1000001
    checked[start] = 1
    while q:
        now_num, cnt = q.popleft()
        if now_num == M:
            return cnt
        for next_num in [now_num + 1, now_num - 1, now_num * 2, now_num - 10]:
            if 0 < next_num <= 1000000 and not checked[next_num]:
                q.append((next_num, cnt + 1))
                checked[next_num] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N)}')
