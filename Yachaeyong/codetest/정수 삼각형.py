'''
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''

N = int(input())
tri = []
for i in range(N):
    num = list(map(int, input().split()))
    tri.append(num)

for r in range(1, N):
    M = len(tri[r])
    for c in range(M):
        if c == 0:
            left = 0
        else:
            left = tri[r-1][c-1]
        if c == r:
            right = 0
        else:
            right = tri[r-1][c]

        tri[r][c] += max(left, right)
ans = 0
for t in tri[N-1]:
    ans = max(ans, t)
print(ans)