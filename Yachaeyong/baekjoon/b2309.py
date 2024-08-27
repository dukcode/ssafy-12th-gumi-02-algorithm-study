# 일곱 난쟁이
# 1. 반복문
data = [int(input()) for _ in range(9)]
data.sort()

fake = []
for i in range(9):
    for j in range(i + 1, 9):
        if len(fake) == 2:
            continue
        if sum(data) - data[i] - data[j] == 100:
            fake.append(data[i])
            fake.append(data[j])

for d in data:
    if d in fake:
        continue
    print(d)

# 2. 재귀
data = [int(input()) for _ in range(9)]
temp = []

def comb(N, idx):
    if N == 7:
        if sum(temp) == 100:
            for i in sorted(temp):
                print(i)
            exit()
        else:
            return

    for i in range(idx, len(data)):
        temp.append(data[i])
        comb(N + 1, idx + 1)
        temp.pop()


comb(0, 0)
