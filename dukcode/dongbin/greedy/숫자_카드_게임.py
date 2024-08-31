h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

ans = 0
for y in range(h):
    ans = max(ans, min(arr[y]))

print(ans)
