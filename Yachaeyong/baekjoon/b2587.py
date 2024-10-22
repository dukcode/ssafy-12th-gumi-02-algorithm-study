# 대표값 2
num = [int(input()) for _ in range(5)]
num.sort()

ans_avg = int(sum(num)/5)
ans_mid = num[2]

print(ans_avg)
print(ans_mid)