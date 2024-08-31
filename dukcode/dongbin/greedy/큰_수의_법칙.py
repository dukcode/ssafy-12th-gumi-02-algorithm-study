n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

first = arr[n - 1]
second = arr[n - 1]

total = (m // (k + 1)) * (k * first + second) + (m % (k + 1)) * first
print(total)
