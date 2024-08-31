n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = 0
first = arr[n - 1]
second = arr[n - 2]

result += (m // (k + 1)) * (first * k + second)
result += (m % (k + 1)) * first

print(result)
