n = int(input())
data = sorted([int(input()) for _ in range(n)])

for i in range(n):
    for j in range(i+1, n):
        if data[i] * (n-i) < data[j] * (n-j):
            break
    else:
        print(data[i] * (n-i))
        break
