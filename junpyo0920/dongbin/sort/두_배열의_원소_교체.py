# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

for i in range(k):
    if arr_a[i] < arr_b[i]:
        arr_a[i] = arr_b[i]
    else:
        break

print(sum(arr_a))
