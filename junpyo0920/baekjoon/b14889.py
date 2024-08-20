# https://www.acmicpc.net/problem/14889

def get_stats(team):
    stats = 0
    for i in range(len(team)):
        for j in range(i, len(team)):
            p1 = team[i]
            p2 = team[j]
            stats += data[p1][p2]
            stats += data[p2][p1]
    return stats


def dfs(t1, cnt=0):
    if len(t1) == N // 2:
        global ans
        t1_stats = get_stats(t1)
        t2 = [i for i in range(N) if i not in t1]
        t2_stats = get_stats(t2)
        ans = min(ans, abs(t1_stats-t2_stats))
        return

    for i in range(cnt, N):
        if i not in t1:
            t1.append(i)
            dfs(t1, i + 1)
            t1.pop()


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
ans = 0xFFFFFFFF
dfs([])
print(ans)
