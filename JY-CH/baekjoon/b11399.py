# ATM
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0

# 내풀이
# 시간 복잡도 n log n + n ** 2
# n번 반복후 합을 계속 다시계산함 n*n
for i in range(1, n + 1):
    result += sum(data[0:i])

result = 0
cur_time = 0

# 다른 풀이 ( 이게 더 좋음 )
# 시간복잡도 n log n
for time in data:
    cur_time += time
    result += cur_time
print(result)