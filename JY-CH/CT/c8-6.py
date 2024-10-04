# 개미 전사
n = int(input())

food = list(map(int, input().split()))

d = [0] * n

d[0] = food[0]
d[1] = max(food[0], food[1])

for idx in range(2, n):
    d[idx] = max(d[idx - 1], d[idx - 2] + food[idx])

print(d[n - 1])

# 점화식을 어떻게 짤것인지 생각하고
# 점화식을 원하는대로 구현하기 연습할것