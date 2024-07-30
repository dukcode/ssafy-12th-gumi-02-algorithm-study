# 최소, 최대

num = int(input())

lst = list(map(int, input().split()))

sorted(lst)

max_value = sorted(lst)[num-1]
min_value = sorted(lst)[0]

print(min_value, max_value)