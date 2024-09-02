'''
3 3
3 1 2
4 1 4
2 2 2
2 4
7 3 1 8
3 3 3 4
'''

# 내 답안

h, w = map(int, input().split())
data = [sorted(list(map(int, input().split()))) for _ in range(h)]

ans = data[0][0]
for y in range(h):
    ans = max(ans, data[y][0])

print(ans)

# 모범 답안

result = 0
for i in range(h):
    data2 = data[i]
    min_value = min(data2)
    result = max(result, min_value)

print(result)
