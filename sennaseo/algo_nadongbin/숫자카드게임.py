h, w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

result = 0
for y in range(h):
    min_num = min(arr[y])

    result = max(result, min_num)

print(result)
