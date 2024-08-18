N = int(input())
line = []
nums = list(map(int, input().split()))

for i in range(N):
    if i == 0:
        line.append(1)
        continue
    idx = len(line) - nums[i]
    line.insert(idx, i + 1)

print(*line)