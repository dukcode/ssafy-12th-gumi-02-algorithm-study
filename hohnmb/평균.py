n = input()
test = list(map(int, input().split()))

test_max = max(test)
test_sum = sum(test)

print(test_sum * 100 / test_max / int(n))
