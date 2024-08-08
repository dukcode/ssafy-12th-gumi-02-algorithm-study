N = int(input())
arr = [int(input()) for _ in range(N)]
max_arr = max(arr)
min_arr = min(arr)

count = [0] * (max_arr + 1)

for i in range(N):
    count[arr[i]] += 1

for i in range(1, max_arr+1):
    count[i] += count[i-1]

temp = [0] * N
for i in range(N-1, -1, -1):
    count[arr[i]] -= 1
    temp[count[arr[i]]] = arr[i]

print(temp)