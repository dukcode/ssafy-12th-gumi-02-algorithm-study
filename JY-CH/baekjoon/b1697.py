# 숨바꼭질
from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        cur_pos = queue.popleft()

        if cur_pos == k:
            return visited[cur_pos]
        
        for move in (cur_pos - 1, cur_pos + 1, cur_pos * 2):
            if 0 <= move <= 100000 and not visited[move]:
                visited[move] = visited[cur_pos] + 1
                queue.append(move)

    return 0

result = bfs()
print(result)

