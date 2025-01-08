# 검증수
data = list(map(int, input().split()))

for i in range(len(data)):
    data[i] = data[i] ** 2

    result = sum(data) % 10

print(result)