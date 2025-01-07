# 간단한 N의 약수

NUM = int(input())
NUM_list = range(1, NUM+1)
result = []
for i in NUM_list:
    if (NUM % i) == 0:
        result.append(i)
print(*result)