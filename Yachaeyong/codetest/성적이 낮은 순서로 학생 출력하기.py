N = int(input())
data = []

for _ in range(N):
    name, grade = input().split()
    data.append((name, grade))

data.sort(key=lambda x: x[1])

for i in range(N):
    print(data[i][0])